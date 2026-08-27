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



def _build_base_context(booking):
    company = CompanyProfile.get_solo()
    service_through = booking.booking_services.select_related("event").all()
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
    return {
        "company_name": company.name,
        "brand_color": company.brand_color,
        "client_name": booking.client_name,
        "services": service_list,
        "original_amount": booking.original_amount,
        "discount_amount": booking.discount_amount,
        "total_amount": booking.total_amount,
        "date": booking.start_time.strftime("%d/%m/%Y"),
        "start_time": booking.start_time.strftime("%H:%M"),
        "end_time": booking.end_time.strftime("%H:%M") if booking.end_time else "",
        "special_requests": booking.special_requests or "",
        "whatsapp_url": _build_whatsapp_url(company.contact_phone),
        "instagram_url": company.instagram_url,
        "tiktok_url": company.tiktok_url,
        "facebook_url": company.facebook_url,
    }


def _build_plain_text(context):
    show_pricing = context.get("show_pricing", True)
    text = (
        f"Hola {context['client_name']},\n\n"
        f"{context['greeting']}\n\n"
        f"Servicios:\n"
    )
    if show_pricing:
        text += "\n".join(
            f"  - {s['name']} ×{s['quantity']} — {s['unit_price']} € "
            f"(Subtotal: {s['subtotal']} €)"
            for s in context["services"]
        )
        text += (
            f"\n\nPrecios:\n"
            f"  Subtotal: {context['original_amount']} €\n"
        )
        if context["discount_amount"] > 0:
            text += f"  Descuento: -{context['discount_amount']} €\n"
        text += f"  Total: {context['total_amount']} €\n\n"
    else:
        text += "\n".join(
            f"  - {s['name']} ×{s['quantity']}"
            for s in context["services"]
        )
        text += "\n\n"
    text += (
        f"Fecha: {context['date']}\n"
        f"Hora: {context['start_time']}"
    )
    if context["end_time"]:
        text += f" - {context['end_time']}"
    text += "\n"
    if context.get("buyer_context"):
        text += f"\n{context['buyer_context']}"
    return text


def _send_email(to_email, subject, context):
    html_content = render_to_string("email/booking_confirmation.html", context)
    plain_text = _build_plain_text(context)
    bcc = [
        addr for addr in getattr(settings, "EMAILS_NOTIFICATIONS", []) or []
        if addr.strip()
    ]
    msg = EmailMultiAlternatives(
        subject=subject,
        body=plain_text,
        from_email=settings.EMAIL_FROM,
        to=[to_email],
        reply_to=[settings.EMAIL_REPLY_TO],
        bcc=bcc,
    )
    msg.attach_alternative(html_content, "text/html")
    msg.send(fail_silently=False)


def send_confirmation_email(booking) -> None:
    try:
        context = _build_base_context(booking)
        context.update({
            "is_gift": False,
            "email_role": "recipient",
            "show_pricing": True,
            "greeting": "Tu cita ha sido confirmada. Aquí tienes los detalles:",
            "gift_buyer_name": booking.buyer_name or booking.client_name,
        })
        _send_email(
            to_email=booking.client_email,
            subject=f"Confirmación de tu cita - {context['company_name']}",
            context=context,
        )
    except Exception:
        logger.exception("Failed to send confirmation email for booking %s", booking.id)


def send_gift_confirmation_emails(booking) -> None:
    recipient_email = booking.recipient_email or booking.client_email
    recipient_name = booking.recipient_name or booking.client_name

    try:
        context = _build_base_context(booking)
        context.update({
            "is_gift": True,
            "email_role": "recipient",
            "show_pricing": False,
            "greeting": f"{booking.buyer_name} te ha regalado una cita. Aquí tienes los detalles:",
            "gift_buyer_name": booking.buyer_name,
            "gift_buyer_email": booking.buyer_email,
            "recipient_name": recipient_name,
            "recipient_email": recipient_email,
        })
        _send_email(
            to_email=recipient_email,
            subject=f"Has recibido un regalo de {booking.buyer_name} - {context['company_name']}",
            context=context,
        )
    except Exception:
        logger.exception("Failed to send gift confirmation email to recipient for booking %s", booking.id)

    try:
        context = _build_base_context(booking)
        context.update({
            "is_gift": True,
            "email_role": "buyer",
            "show_pricing": True,
            "greeting": f"Has regalado una cita a {recipient_name}.",
            "gift_buyer_name": booking.buyer_name,
            "gift_buyer_email": booking.buyer_email,
            "recipient_name": recipient_name,
            "recipient_email": recipient_email,
            "client_name": booking.buyer_name,
        })
        _send_email(
            to_email=booking.buyer_email,
            subject=f"Has regalado una cita a {recipient_name} - {context['company_name']}",
            context=context,
        )
    except Exception:
        logger.exception("Failed to send gift confirmation email to buyer for booking %s", booking.id)