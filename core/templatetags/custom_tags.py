from django import template

register = template.Library()


@register.filter
def lowfirst_list(values: list) -> list:
    res = []
    for item in values:
        if item:
            res.append(item[0].lower() + item[1:])
        else:
            res.append(item)
    return res
