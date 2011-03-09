from django.conf import settings
from django import template

register = template.Library()

@register.filter
def variant_price(variant, currency=getattr(settings, 'SATCHLESS_DEFAULT_CURRENCY', None)):
    if not currency:
        return ''
    try:
        from satchless.pricing.handler import get_variant_price
        price = get_variant_price(variant, currency)
        if price is not None and price.has_value():
            return price
    except ImportError:
        pass
    return ''

@register.filter
def product_price_range(product, currency=getattr(settings, 'SATCHLESS_DEFAULT_CURRENCY', None)):
    if not currency:
        return ''
    try:
        from satchless.pricing.handler import get_product_price_range
        price_range = get_product_price_range(product, currency)
        if price_range['min'] is not None and price_range['min'].has_value():
            return price_range
    except ImportError:
        pass
    return ''
