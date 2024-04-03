from django import template
from django.urls import translate_url

register = template.Library()


@register.filter
def lowfirst_list(values: list) -> list:
    res = []
    for item in values:
        if item and len(item) > 1 and not item.isupper():
            res.append(item[0].lower() + item[1:])
        else:
            res.append(item)
    return res


@register.simple_tag(takes_context=True)
def change_language(context, lang=None, *args, **kwargs):
    path = context['request'].get_full_path()
    return translate_url(path, lang)
