from django.http import JsonResponse
from django.contrib.admin.views.decorators import staff_member_required

from .models import Case

from datetime import datetime


@staff_member_required
def cases_count(request, mediator_pk: int) -> JsonResponse:
    """Повертає кількість справ медіатора за період."""
    try:
        date_from = datetime.strptime(request.GET.get('date_from'), '%Y-%m-%d')
        date_to = datetime.strptime(request.GET.get('date_to'), '%Y-%m-%d')
    except ValueError:
        return JsonResponse({'result': 'error', 'msg': 'отримано невірні значення параметрів'})
    count = Case.objects.filter(
        mediator_id=mediator_pk,
        case_date__gte=date_from,
        case_date__lte=date_to,
    ).count()
    return JsonResponse({'result': 'success', 'count': count})
