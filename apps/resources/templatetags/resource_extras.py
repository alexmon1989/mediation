from django import template

from ..models import Resource

from typing import List


register = template.Library()


@register.simple_tag
def resources_active() -> List[dict]:
    """Повертає список активних ресурсів (тільки title, slug)"""
    return Resource.objects.filter(enabled=True).values('title', 'slug')
