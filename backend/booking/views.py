from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.conf import settings
from .models import CompanyProfile, CompanyWeekdaySlot, EventType
from .serializers import CompanyProfileSerializer, BusinessHoursSerializer, EventTypeSerializer
from utils.availability import get_available_dates

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
            
        available_dates = get_available_dates(ids)
        return Response(available_dates)
