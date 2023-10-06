from django import template

from ..models import Contact


register = template.Library()


@register.simple_tag
def contacts_data() -> Contact:
    """Повертає контактні дані."""
    return Contact.objects.first()
