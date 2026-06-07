from django.db import transaction
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from datetime import timedelta
from .models import Booking, BookingServiceThrough
from utils.google_calendar import sync_booking_to_google, delete_google_calendar_event


@receiver(post_save, sender=BookingServiceThrough)
def update_booking_from_through(sender, instance, **kwargs):
    """Recalculate booking end_time when through model changes."""
    booking = instance.booking
    if booking and booking.start_time:
        total_duration = sum(
            bs.quantity * bs.event.duration_minutes
            for bs in booking.booking_services.all()
        )
        booking.end_time = booking.start_time + timedelta(minutes=total_duration)
        booking.save(update_fields=["end_time"])

    if booking and booking.status != "PENDING" and booking.booking_services.exists():
        transaction.on_commit(lambda: sync_booking_to_google(booking))


@receiver(post_delete, sender=BookingServiceThrough)
def update_booking_on_delete(sender, instance, **kwargs):
    """Recalculate booking end_time when through model row is deleted."""
    booking = instance.booking
    if booking and booking.start_time:
        total_duration = sum(
            bs.quantity * bs.event.duration_minutes
            for bs in booking.booking_services.all()
        )
        booking.end_time = booking.start_time + timedelta(minutes=total_duration)
        booking.save(update_fields=["end_time"])


@receiver(post_save, sender=Booking)
def booking_post_save(sender, instance, created, **kwargs):
    # Skip sync if ONLY internal Google fields or end_time are updated.
    # end_time is in the skip-set because the m2m_changed handler and
    # Booking.save()'s recomputation both save with update_fields containing end_time.
    # m2m_changed is the primary sync trigger for service/time changes.
    skip_fields = {
        "google_event_id",
        "google_sync_status",
        "google_sync_error",
        "last_synced_at",
        "end_time",
    }
    if kwargs.get("update_fields") and set(kwargs["update_fields"]) <= skip_fields:
        return

    # Transition to CANCELLED
    if (
        instance.status == "CANCELLED"
        and instance._initial_status != "CANCELLED"
        and instance.google_event_id
    ):
        transaction.on_commit(lambda: sync_booking_to_google(instance))
        return

    # Skip sync if status is PENDING.
    # We only sync when confirmed or paid.
    if instance.status == "PENDING":
        return

    # Otherwise, schedule sync
    transaction.on_commit(lambda: sync_booking_to_google(instance))


@receiver(post_delete, sender=Booking)
def booking_post_delete(sender, instance, **kwargs):
    delete_google_calendar_event(instance)
