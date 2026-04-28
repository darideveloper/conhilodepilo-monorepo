import { describe, it, expect } from 'vitest';
import { formatPhoneForWhatsApp, formatPhoneForDisplay } from './phone';

describe('phone utilities', () => {
  describe('formatPhoneForWhatsApp', () => {
    it('should strip all non-numeric characters', () => {
      expect(formatPhoneForWhatsApp('+34 915 23 14 06')).toBe('34915231406');
      expect(formatPhoneForWhatsApp('915-23-14-06')).toBe('915231406');
    });

    it('should handle null or undefined', () => {
      expect(formatPhoneForWhatsApp(null)).toBe('');
      expect(formatPhoneForWhatsApp(undefined)).toBe('');
    });

    it('should return empty string for empty input', () => {
      expect(formatPhoneForWhatsApp('')).toBe('');
    });
  });

  describe('formatPhoneForDisplay', () => {
    it('should format Spanish landlines (starting with 9 or 8)', () => {
      expect(formatPhoneForDisplay('915231406')).toBe('915 23 14 06');
      expect(formatPhoneForDisplay('815231406')).toBe('815 23 14 06');
    });

    it('should format Spanish mobiles (starting with 6 or 7)', () => {
      expect(formatPhoneForDisplay('600000000')).toBe('600 000 000');
      expect(formatPhoneForDisplay('700000000')).toBe('700 000 000');
    });

    it('should return trimmed string if not 9 digits', () => {
      expect(formatPhoneForDisplay('12345678')).toBe('12345678');
      expect(formatPhoneForDisplay('1234567890')).toBe('1234567890');
    });

    it('should handle null or undefined', () => {
      expect(formatPhoneForDisplay(null)).toBe('');
      expect(formatPhoneForDisplay(undefined)).toBe('');
    });
  });
});
