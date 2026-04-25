import os
import re
import colorsys
from django.templatetags.static import static
from booking.models import CompanyProfile

def environment_callback(request):
    env = os.getenv("ENV", "dev")
    env_mapping = {
        "prod": ["Production", "danger"],
        "staging": ["Staging", "warning"],
        "dev": ["Development", "info"],
        "local": ["Local", "success"],
    }
    return env_mapping.get(env, ["Unknown", "info"])

def get_company():
    return CompanyProfile.get_solo()

def site_title_callback(request):
    return get_company().name

def site_header_callback(request):
    return get_company().name

def site_icon_callback(request):
    company = get_company()
    if company.logo:
        return company.logo.url
    return static("favicon.png")

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    if len(hex_color) == 3:
        hex_color = ''.join([c*2 for c in hex_color])
    return tuple(int(hex_color[i:i+2], 16) / 255.0 for i in (0, 2, 4))

def rgb_to_oklch_approx(r, g, b):
    # Very rough approximation to HSL for generating variants
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    # Map HSL roughly to OKLCH ranges for generation
    return (l, s * 0.3, h * 360)

def get_brand_config():
    """Derives a full range of shades for CSS variables."""
    base_color = get_company().brand_color
    
    match = re.match(r"oklch\(([\d.]+%?) ([\d.]+) ([\d.]+)\)", base_color)
    
    if match:
        l_str, c_str, h_str = match.groups()
        l = float(l_str.rstrip('%')) / 100.0 if '%' in l_str else float(l_str)
        c = float(c_str)
        h = float(h_str)
    else:
        try:
            r, g, b = hex_to_rgb(base_color)
            l, c, h = rgb_to_oklch_approx(r, g, b)
            # Normalize h if it's 360 to keep it consistent
        except Exception:
            l, c, h = 0.68, 0.28, 296 # Fallback to default
            
    # Luminance targets for Tailwind-like shades
    shades = {
        "50": 0.97, "100": 0.92, "200": 0.85, "300": 0.75, 
        "400": min(l + 0.1, 0.9), "500": l, "600": max(l - 0.1, 0.1), 
        "700": max(l - 0.2, 0.05), "800": max(l - 0.3, 0.02), 
        "900": max(l - 0.4, 0.01), "950": max(l - 0.5, 0.0)
    }
    
    result = {}
    for shade, target_l in shades.items():
        if shade in ["500", "600"]:
            result[shade] = base_color
            continue
            
        current_c = c
        if target_l > 0.8: current_c *= 0.3
        elif target_l < 0.3: current_c *= 0.8
        
        result[shade] = f"oklch({target_l:.3f} {current_c:.3f} {h:.1f})"
    return result
