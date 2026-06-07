from decimal import Decimal
from django.db import transaction
from django.db.utils import IntegrityError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone
from datetime import datetime, time
import stripe
from .models import CompanyProfile, CompanyWeekdaySlot, EventType, Event, Booking, BookingServiceThrough, ProcessedStripeEvent
from .serializers import CompanyProfileSerializer, BusinessHoursSerializer, EventTypeSerializer
from utils.availability import get_available_dates, get_available_slots
from utils.stripe_utils import create_checkout_session
from utils.google_calendar import sync_booking_to_google
from utils.email import send_confirmation_email
from utils.pricing import calculate_booking_totals

class CreateBookingView(APIView):
    """
    Public endpoint to create a new booking.
    """
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        services_input = request.data.get('services')
        date_str = request.data.get('date')
        start_time_str = request.data.get('startTime')
        client_name = request.data.get('clientName')
        client_email = request.data.get('clientEmail')
        client_phone = request.data.get('clientPhone')
        special_requests = request.data.get('specialRequests', "")

        if not all([services_input, date_str, start_time_str, client_name, client_email]):
            return Response({"error": "Missing required fields"}, status=400)

        if not isinstance(services_input, list):
            return Response({"error": "services must be a list of {service_id, quantity}"}, status=400)

        parsed_services = []
        for s in services_input:
            if not isinstance(s, dict):
                return Response({"error": "Each service must be an object with service_id and quantity"}, status=400)
            service_id = s.get('service_id')
            quantity = s.get('quantity', 1)
            if not service_id:
                return Response({"error": "service_id is required for each service"}, status=400)
            try:
                sid = int(service_id)
                qty = int(quantity)
                if qty < 1:
                    return Response({"error": "quantity must be at least 1"}, status=400)
                parsed_services.append((sid, qty))
            except (ValueError, TypeError):
                return Response({"error": "Invalid service_id or quantity format"}, status=400)

        try:
            target_date = datetime.strptime(date_str, '%Y-%m-%d').date()
            start_time = datetime.strptime(start_time_str, '%H:%M').time()
        except (ValueError, TypeError):
            return Response({"error": "Invalid format for date or startTime"}, status=400)

        service_ids = [s[0] for s in parsed_services]
        quantities = {s[0]: s[1] for s in parsed_services}

        events = {e.id: e for e in Event.objects.filter(id__in=service_ids)}
        if len(events) != len(service_ids):
            return Response({"error": "One or more services not found"}, status=400)

        for sid in service_ids:
            if sid not in events:
                return Response({"error": f"Service {sid} not found"}, status=400)

        available_slots = get_available_slots(target_date, service_ids, quantities)
        if start_time_str not in available_slots:
            return Response({"error": "Selected time slot is no longer available"}, status=400)

        start_dt = timezone.make_aware(datetime.combine(target_date, start_time))

        booking_services_for_pricing = []
        total_duration = 0
        for sid, qty in parsed_services:
            event = events[sid]
            booking_services_for_pricing.append((event, qty, event.price))
            total_duration += event.duration_minutes * qty

        original_amount, discount_amount, total_amount, _ = calculate_booking_totals(booking_services_for_pricing)
        end_dt = start_dt + timezone.timedelta(minutes=total_duration)

        is_pre_paid = any(events[sid].event_type.payment_model == "PRE-PAID" for sid in service_ids)
        status = "PENDING" if is_pre_paid else "CONFIRMED"

        try:
            with transaction.atomic():
                booking = Booking.objects.create(
                    start_time=start_dt,
                    end_time=end_dt,
                    client_name=client_name,
                    client_email=client_email,
                    client_phone=client_phone,
                    special_requests=special_requests,
                    status=status,
                    original_amount=original_amount,
                    discount_amount=discount_amount,
                    total_amount=total_amount
                )

                through_rows = []
                for sid, qty in parsed_services:
                    event = events[sid]
                    through_rows.append(BookingServiceThrough(
                        booking=booking,
                        event=event,
                        quantity=qty,
                        unit_price=event.price
                    ))
                BookingServiceThrough.objects.bulk_create(through_rows)

                if status == "CONFIRMED":
                    transaction.on_commit(lambda: sync_booking_to_google(booking))
                    transaction.on_commit(lambda b=booking: send_confirmation_email(b))

                response_data = {
                    "message": "Booking created successfully",
                    "booking_id": booking.id,
                    "client_name": booking.client_name,
                    "client_email": booking.client_email,
                    "start_time": booking.start_time.isoformat(),
                    "payment_required": is_pre_paid,
                    "original_amount": str(original_amount),
                    "discount_amount": str(discount_amount),
                    "total_amount": str(total_amount)
                }

                if is_pre_paid:
                    if total_amount > 0:
                        company = CompanyProfile.get_solo()
                        try:
                            session = create_checkout_session(booking, total_amount, company.currency)
                            response_data["checkout_url"] = session.url
                        except stripe.StripeError:
                            raise Exception("Stripe session creation failed")
                    else:
                        response_data["payment_required"] = False

        except Exception as e:
            if "Stripe" in str(e):
                return Response({"error": "Payment service is currently unavailable. Please try again later."}, status=503)
            raise e

        return Response(response_data, status=201)

class CompanyConfigView(APIView):
    """
    Public endpoint to fetch company branding, contact details, and UI labels.
    """
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        config = CompanyProfile.get_solo()
        serializer = CompanyProfileSerializer(config, context={'request': request})
        data = serializer.data
        
        # Inject system timezone
        data['timezone'] = settings.TIME_ZONE
        
        return Response(data)

class BusinessHoursView(APIView):
    """
    Public endpoint to fetch company business hours (weekday slots).
    """
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        config = CompanyProfile.get_solo()
        slots = config.weekday_slots.all().order_by('weekday', 'start_time')
        serializer = BusinessHoursSerializer(slots, many=True)
        return Response(serializer.data)

class ServicesListView(APIView):
    """
    Public endpoint to fetch all service categories and their associated services.
    """
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        categories = EventType.objects.prefetch_related('events').all()
        serializer = EventTypeSerializer(categories, many=True, context={'request': request})
        return Response(serializer.data)

class AvailabilityView(APIView):
    """
    Public endpoint to check available days for selected services.
    """
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        service_ids = request.query_params.get('service_ids')
        if not service_ids:
            return Response({"error": "service_ids is required"}, status=400)

        try:
            ids = [int(sid) for sid in service_ids.split(',')]
        except ValueError:
            return Response({"error": "Invalid service_ids format"}, status=400)

        quantities_param = request.query_params.get('quantities')
        quantities = None
        if quantities_param:
            try:
                q_list = [int(q) for q in quantities_param.split(',')]
                if len(q_list) != len(ids):
                    return Response({"error": "quantities length must match service_ids length"}, status=400)
                if any(q < 1 for q in q_list):
                    return Response({"error": "quantities must be positive integers"}, status=400)
                quantities = dict(zip(ids, q_list))
            except ValueError:
                return Response({"error": "Invalid quantities format"}, status=400)

        available_dates = get_available_dates(ids, quantities=quantities)
        return Response(available_dates)


class AvailabilitySlotsView(APIView):
    """
    Public endpoint to check available time slots for selected services on a specific date.
    """
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        service_ids = request.query_params.get('service_ids')
        date_str = request.query_params.get('date')

        if not service_ids or not date_str:
            return Response({"error": "service_ids and date are required"}, status=400)

        try:
            ids = [int(sid) for sid in service_ids.split(',')]
            target_date = datetime.strptime(date_str, '%Y-%m-%d').date()
        except (ValueError, TypeError):
            return Response({"error": "Invalid service_ids or date format (YYYY-MM-DD)"}, status=400)

        quantities_param = request.query_params.get('quantities')
        quantities = None
        if quantities_param:
            try:
                q_list = [int(q) for q in quantities_param.split(',')]
                if len(q_list) != len(ids):
                    return Response({"error": "quantities length must match service_ids length"}, status=400)
                if any(q < 1 for q in q_list):
                    return Response({"error": "quantities must be positive integers"}, status=400)
                quantities = dict(zip(ids, q_list))
            except ValueError:
                return Response({"error": "Invalid quantities format"}, status=400)

        slots = get_available_slots(target_date, ids, quantities)
        return Response(slots)

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

@method_decorator(csrf_exempt, name='dispatch')
class StripeWebhookView(APIView):
    """
    Public endpoint to handle Stripe webhooks.
    """
    permission_classes = [AllowAny]
    authentication_classes = []

    def post(self, request, *args, **kwargs):
        payload = request.body
        sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')
        endpoint_secret = settings.STRIPE_WEBHOOK_SECRET

        if not endpoint_secret:
            return Response({"error": "Webhook secret not configured"}, status=400)

        try:
            event = stripe.Webhook.construct_event(
                payload, sig_header, endpoint_secret
            )
        except ValueError as e:
            # Invalid payload
            return Response(status=400)
        except stripe.SignatureVerificationError as e:
            # Invalid signature
            return Response(status=400)

        try:
            with transaction.atomic():
                ProcessedStripeEvent.objects.create(event_id=event.id)
        except IntegrityError:
            return Response(status=200)

        # Handle the event
        if event.type == 'checkout.session.completed':
            session = event.data.object
            booking_id = getattr(session.metadata, 'booking_id', None) if session.metadata else None
            if booking_id:
                try:
                    booking = Booking.objects.get(id=booking_id)
                    if booking.status == 'PENDING':
                        booking.status = 'PAID'
                        booking.stripe_payment_id = session.payment_intent or session.id
                        booking.save(update_fields=['status', 'stripe_payment_id'])
                        transaction.on_commit(lambda b=booking: send_confirmation_email(b))
                        
                        # Note: Google Calendar sync will be triggered by a signal
                except Booking.DoesNotExist:
                    pass

        return Response(status=200)


class TestEmailView(APIView):
    """
    Debug endpoint to verify SMTP credentials are working.

    Sends a plain-text test email using the SMTP configuration defined in
    environment variables (EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_USER, etc.).

    GET Parameters:
        to (str, required): Comma-separated list of recipient email addresses.

    Responses:
        200: {"message": "Test email sent successfully", "to": [...]}
        400: {"error": "Missing 'to' query parameter..."}
        500: {"error": "Failed to send email: <SMTP error detail>"}

    Usage:
        GET /api/test-email/?to=user@example.com
        GET /api/test-email/?to=alice@test.com,bob@test.com
    """
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        to_emails = request.query_params.get("to", "")
        if not to_emails:
            return Response(
                {"error": "Missing 'to' query parameter with comma-separated emails"},
                status=400
            )

        email_list = [e.strip() for e in to_emails.split(",") if e.strip()]
        if not email_list:
            return Response({"error": "No valid email addresses provided"}, status=400)

        try:
            send_mail(
                subject="Test Email from Con Hilo Depilo",
                message=(
                    "This is a test email to verify SMTP configuration.\n\n"
                    "If you received this, the email system is working correctly."
                ),
                from_email=settings.EMAIL_FROM,
                recipient_list=email_list,
                fail_silently=False,
            )
            return Response({
                "message": "Test email sent successfully",
                "to": email_list,
            })
        except Exception as e:
            return Response(
                {"error": f"Failed to send email: {str(e)}"},
                status=500
            )
