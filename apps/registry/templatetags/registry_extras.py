from django import template

from ..models import Mediator

register = template.Library()


@register.simple_tag(takes_context=True)
def mediator_name(context, mediator: Mediator, *args, **kwargs):
    lang = context['request'].LANGUAGE_CODE
    res = f"{mediator.last_name} {mediator.first_name}"
    if lang == 'uk' and mediator.middle_name_uk:
        res = f"{res} {mediator.middle_name_uk}"
    elif lang == 'en' and mediator.middle_name_en:
        res = f"{res} {mediator.middle_name_en}"
    return res
