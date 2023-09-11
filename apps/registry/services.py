from django.db.models import QuerySet, Value
from django.db.models.functions import Concat
from .models import Mediator


def get_mediators_qs(only_active: bool = True, filters: dict = None) -> QuerySet[Mediator]:
    """Повертає Queryset з медіаторами."""
    res = Mediator.objects.order_by(
        'last_name',
        'first_name',
        'middle_name'
    )
    if only_active:
        res = res.filter(active=True)

    # Пошук
    if filters:
        if filters.get('mediator_name'):
            res = res.annotate(
                search_name=Concat('last_name', Value(' '), 'first_name', Value(' '), 'middle_name')
            ).filter(search_name__icontains=filters['mediator_name'])

        if filters.get('region'):
            regions = [filters['region']]
            if filters['region'] != 1:
                regions.append(1)
            res = res.filter(regions__in=regions)

        if filters.get('specialization'):
            specialization = [filters['specialization']]
            if filters['specialization'] != 1:
                specialization.append(1)
            res = res.filter(specializations__in=specialization)

        if filters.get('work_format'):
            res = res.filter(work_format=filters['work_format'])

    return res
