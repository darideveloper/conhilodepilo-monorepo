"""
Management command to test the booking confirmation email.

Creates a temporary booking with sample data, sends the confirmation email
to a specified recipient, then cleans up.

**Email by terminal (interactive mode):**
If you run the command without providing an email argument, it will prompt
you interactively to enter one. This is useful for quick ad-hoc testing:

    python manage.py test_email
    → Enter recipient email: user@example.com

Usage:
    python manage.py test_email                          # interactive prompt
    python manage.py test_email user@example.com          # direct argument
    EMAIL_TO=user@example.com python manage.py test_email # env variable
    python manage.py test_email user@example.com --no-send  # dry-run
"""
from django.core.management.base import BaseCommand, CommandError
from decimal import Decimal
from django.utils import timezone
from booking.models import Booking, BookingServiceThrough, Event, CompanyProfile
from utils.email import send_confirmation_email


class Command(BaseCommand):
    help = "Send a test booking confirmation email to a custom recipient"

    def add_arguments(self, parser):
        parser.add_argument("email", nargs="?", help="Recipient email address (optional — prompts if omitted)")
        parser.add_argument(
            "--no-send",
            action="store_true",
            help="Dry-run: create booking but skip sending the email",
        )

    def handle(self, *args, **options):
        recipient = options["email"]

        # Resolve recipient: arg > env > terminal prompt
        if not recipient:
            recipient = __import__("os").environ.get("EMAIL_TO")
        if not recipient:
            try:
                recipient = input("Enter recipient email: ").strip()
            except (EOFError, KeyboardInterrupt):
                raise CommandError("No recipient provided. Use: python manage.py test_email user@example.com")

        if not recipient:
            raise CommandError("Email address is required.")

        event = Event.objects.first()
        if not event:
            raise CommandError("No services (Event) found in the database. Create one in the admin first.")

        cp = CompanyProfile.get_solo()
        cp.buy_x = 2
        cp.get_y_free = 1
        cp.save()

        booking = Booking.objects.create(
            client_name="Test User",
            client_email="test@example.com",
            client_phone="+34 600 000 000",
            start_time=timezone.now(),
            end_time=timezone.now() + timezone.timedelta(minutes=event.duration_minutes * 3),
            status="CONFIRMED",
            original_amount=Decimal("90.00"),
            discount_amount=Decimal("30.00"),
            total_amount=Decimal("60.00"),
        )

        BookingServiceThrough.objects.create(
            booking=booking, event=event, quantity=3, unit_price=event.price
        )

        self.stdout.write(f"Booking #{booking.id} created")

        try:
            if options["no_send"]:
                self.stdout.write(f"[DRY-RUN] Would send confirmation email to: {recipient}")
                return

            booking.client_email = recipient
            send_confirmation_email(booking)
            self.stdout.write(self.style.SUCCESS(f"✓ Confirmation email sent to: {recipient}"))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"✗ FAILED to send email: {e}"))
            raise
        finally:
            booking.delete()
            self.stdout.write("Test booking cleaned up.\n")
