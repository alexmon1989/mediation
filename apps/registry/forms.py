from django import forms
from django.utils.translation import gettext_lazy as _

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Field, Div

from .models import Region, Specialization, WorkFormat, CHANGE_REASON_CHOICES

from datetime import datetime


class MediatorModelForm(forms.ModelForm):
    change_reason = forms.ChoiceField(
        choices=CHANGE_REASON_CHOICES,
        required=False,
        label='Причина змін',
        help_text='В залежності від обраного значення буде чи не буде змінено значення поля "Дата останнього оновлення"'
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['change_reason'].required = True

    def save(self, commit=True):
        change_reason = self.cleaned_data.get('change_reason', None)
        instance = super().save(commit=False)
        if change_reason:
            instance.last_change_reason = change_reason
            if change_reason == 'biblio':
                instance.updated_at = datetime.now()
        return instance


class SearchForm(forms.Form):
    """Форма пошуку."""
    mediator_name = forms.CharField(
        label=_("Прізвище, ім'я, по батькові"),
        max_length=255,
        widget=forms.TextInput(attrs={'placeholder': _('ПІБ медіатора')}),
        required=False,
    )
    region = forms.ModelChoiceField(
        queryset=Region.objects.order_by('weight', 'title'),
        label=_('Регіон роботи'),
        required=False,
    )
    specialization = forms.ModelChoiceField(
        queryset=Specialization.objects.order_by('weight', 'title'),
        label=_('Спеціалізація'),
        required=False,
    )
    work_format = forms.ModelChoiceField(
        queryset=WorkFormat.objects.order_by('weight', 'title'),
        label=_('Формат роботи'),
        required=False,
    )

    @property
    def submitted(self) -> bool:
        """Чи була форма відправлена."""
        return bool(set(self.data.keys()) & set(self.fields.keys()))  # перетин множин

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'GET'
        self.helper.layout = Layout(
            Row(
                Column(
                    Field('mediator_name', css_class='form-control form-control-sm'),
                    css_class='col-md-12'
                ),
                # Column(
                #     Field('specialization', css_class='form-select form-select-sm'),
                #     css_class='col-md-6'
                # ),
            ),
            Row(
                Column(
                    Field('region', css_class='form-select form-select-sm'),
                   css_class='col-md-6'
                ),
                Column(
                    Field('work_format', css_class='form-select form-select-sm'),
                    css_class='col-md-6'
                ),
            ),
            Div(template='registry/list/_partials/submit.html')
        )
