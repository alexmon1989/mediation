from django.db.models import QuerySet
from .models import Resource


def get_resources_qs(only_enabled: bool = True) -> QuerySet[Resource]:
    """Повертає Queryset з ресурсами."""
    res = Resource.objects.all()
    if only_enabled:
        res = res.filter(enabled=True)
    return res
