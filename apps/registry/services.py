from django.db.models import QuerySet, Value, Q, CharField
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
                search_name_uk=Concat(
                    'last_name_uk', Value(' '), 'first_name_uk', Value(' '), 'middle_name_uk', output_field=CharField(),
                ),
                search_name_en=Concat(
                    'last_name_en', Value(' '), 'first_name_en', Value(' '), 'middle_name_en', output_field=CharField(),
                ),
            ).filter(
                Q(search_name_uk__icontains=filters['mediator_name']) |
                Q(search_name_en__icontains=filters['mediator_name'])
            )

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
