/**
 * Formats a phone number for use in WhatsApp links (wa.me).
 * Removes all non-numeric characters.
 */
export function formatPhoneForWhatsApp(phone: string | null | undefined): string {
  if (!phone) return "";
  return phone.replace(/\D/g, "");
}

/**
 * Formats a phone number for consistent display.
 * Example: 915231406 -> 915 23 14 06
 * If it looks like a Spanish landline (9 digits starting with 9), it groups by 3.
 * Otherwise, it returns the trimmed string.
 */
export function formatPhoneForDisplay(phone: string | null | undefined): string {
  if (!phone) return "";
  const cleaned = phone.trim();
  
  // Basic formatting for Spanish 9-digit numbers
  if (cleaned.length === 9 && (cleaned.startsWith('9') || cleaned.startsWith('8'))) {
    return cleaned.replace(/(\d{3})(\d{2})(\d{2})(\d{2})/, "$1 $2 $3 $4");
  }
  
  // Basic formatting for 9-digit mobiles
  if (cleaned.length === 9 && (cleaned.startsWith('6') || cleaned.startsWith('7'))) {
     return cleaned.replace(/(\d{3})(\d{3})(\d{3})/, "$1 $2 $3");
  }

  return cleaned;
}
