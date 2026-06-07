from django.db import migrations, models


def backfill_gift_fields(apps, schema_editor):
    Booking = apps.get_model("booking", "Booking")
    Booking.objects.filter(buyer_name__isnull=True).update(
        is_gift=False,
        buyer_name=models.F("client_name"),
        buyer_email=models.F("client_email"),
    )


def reverse_backfill(apps, schema_editor):
    Booking = apps.get_model("booking", "Booking")
    Booking.objects.filter(is_gift=False).update(
        buyer_name=None,
        buyer_email=None,
    )


class Migration(migrations.Migration):

    dependencies = [
        ("booking", "0018_add_gift_fields_to_booking"),
    ]

    operations = [
        migrations.RunPython(backfill_gift_fields, reverse_backfill),
    ]
