from utils.callbacks import get_brand_config, site_title_callback, site_header_callback

def brand_theme_context(request):
    return {
        "brand_colors": get_brand_config(),
        "site_title": site_title_callback(request),
        "site_header": site_header_callback(request),
    }
