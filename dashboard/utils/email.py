import logging
import re
from decimal import Decimal

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from booking.models import CompanyProfile

logger = logging.getLogger(__name__)


def _clean_phone(phone: str | None) -> str:
    if not phone:
        return ""
    return re.sub(r"\D", "", phone)


def _build_whatsapp_url(phone: str | None) -> str | None:
    digits = _clean_phone(phone)
    if not digits:
        return None
    return f"https://wa.me/{digits}"


def _build_logo_url(company: CompanyProfile) -> str | None:
    if company.logo:
        host = getattr(settings, "HOST", "")
        if host and "localhost" not in host:
            return f"{host.rstrip('/')}{company.logo.url}"
    return None


def send_confirmation_email(booking) -> None:
    try:
        company = CompanyProfile.get_solo()
        whatsapp_url = _build_whatsapp_url(company.contact_phone)
        logo_url = _build_logo_url(company)

        service_through = booking.booking_services.select_related('event').all()
        service_list = [
            {
                "name": bs.event.name,
                "unit_price": bs.unit_price,
                "quantity": bs.quantity,
                "subtotal": bs.unit_price * Decimal(str(bs.quantity)),
                "duration_minutes": bs.event.duration_minutes,
            }
            for bs in service_through
        ]

        context = {
            "company_name": company.name,
            "brand_color": company.brand_color,
            "logo_url": logo_url,
            "client_name": booking.client_name,
            "services": service_list,
            "original_amount": booking.original_amount,
            "discount_amount": booking.discount_amount,
            "total_amount": booking.total_amount,
            "date": booking.start_time.strftime("%d/%m/%Y"),
            "start_time": booking.start_time.strftime("%H:%M"),
            "end_time": booking.end_time.strftime("%H:%M") if booking.end_time else "",
            "special_requests": booking.special_requests or "",
            "whatsapp_url": whatsapp_url,
            "instagram_url": company.instagram_url,
            "tiktok_url": company.tiktok_url,
            "facebook_url": company.facebook_url,
        }

        html_content = render_to_string("email/booking_confirmation.html", context)

        subject = f"Confirmación de tu cita - {company.name}"
        plain_text = (
            f"Hola {booking.client_name},\n\n"
            f"Tu cita ha sido confirmada.\n\n"
            f"Servicios:\n"
            + "\n".join(
                f"  - {s['name']} ×{s['quantity']} — {s['unit_price']} € "
                f"(Subtotal: {s['subtotal']} €)"
                for s in service_list
            )
            + f"\n\nPrecios:\n"
            f"  Subtotal: {context['original_amount']} €\n"
        )
        if context["discount_amount"] > 0:
            plain_text += f"  Descuento: -{context['discount_amount']} €\n"
        plain_text += (
            f"  Total: {context['total_amount']} €\n\n"
            f"Fecha: {context['date']}\n"
            f"Hora: {context['start_time']}"
        )
        if context["end_time"]:
            plain_text += f" - {context['end_time']}"
        plain_text += "\n"

        bcc = [
            addr for addr in getattr(settings, "EMAILS_NOTIFICATIONS", []) or []
            if addr.strip()
        ]

        msg = EmailMultiAlternatives(
            subject=subject,
            body=plain_text,
            from_email=settings.EMAIL_FROM,
            to=[booking.client_email],
            bcc=bcc,
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send(fail_silently=False)

    except Exception:
        logger.exception("Failed to send confirmation email for booking %s", booking.id)