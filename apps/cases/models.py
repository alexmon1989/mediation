from django.db import models
from apps.registry.models import Mediator
from apps.common.models import TimeStampModel


class Case(TimeStampModel):
    """Модель справи."""
    case_number = models.CharField('Номер справи', max_length=255)
    case_date = models.DateField('Дата справи')
    mediator = models.ForeignKey(Mediator, on_delete=models.SET_NULL, blank=False, null=True, verbose_name='Медіатор')

    def __str__(self) -> str:
        return self.case_number

    class Meta:
        verbose_name = 'Справа'
        verbose_name_plural = 'Справи'
        db_table = 'cases_list'
