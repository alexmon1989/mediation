from django.contrib import admin
from django.db import models
from django.forms import Textarea
from django.urls import resolve

from reversion.admin import VersionAdmin
from singlemodeladmin import SingleModelAdmin

from .models import Mediator, Page
from .forms import MediatorModelForm


class EducationInline(admin.StackedInline):
    model = Mediator.educations.through
    extra = 1


class TrainingInline(admin.StackedInline):
    model = Mediator.trainings.through
    extra = 1
    verbose_name_plural = 'Підготовка'
    autocomplete_fields = (
        'education_institution',
        'education_course'
    )

@admin.register(Mediator)
class MediatorAdmin(VersionAdmin):
    form = MediatorModelForm
    save_on_top = True
    ordering = ('pk',)
    list_display = (
        'last_name',
        'first_name',
        'middle_name',
        'active',
        'created_at',
        'updated_at'
    )
    search_fields = (
        'last_name',
        'first_name',
        'middle_name',
    )
    list_filter = (
        'active',
    )
    inlines = [
        EducationInline,
        TrainingInline,
    ]
    autocomplete_fields = (
        'specialities',
        'specializations',
        'languages',
        'regions',
        'professional_directions',
    )
    fieldsets = [
        (
            None,
            {
                "fields": [],
            },
        ),
        (
            "Контактна інформація",
            {
                "fields": [
                    "address",
                    "email",
                    "phones",
                ],
            },
        ),
        (
            "Додаткова інформація",
            {
                "fields": [
                    "job",
                    "job_experience",
                    "mediators_membership",
                    "awards",
                    "price",
                    "other",
                ],
            },
        ),
    ]
    formfield_overrides = {
        models.TextField: {'widget': Textarea(
            attrs={'rows': 2})},
    }
    readonly_fields = ('updated_at',)

    def get_fieldsets(self, request, obj=None):
        fields = [
            "updated_at",
            "application_number",
            "application_date",
            "last_name",
            "first_name",
            "middle_name",
            "photo",
            "languages",
            "specialities",
            "specializations",
            "work_format",
            "regions",
            "professional_directions",
            "active",
        ]
        current_url = resolve(request.path_info).url_name
        if obj:
            if current_url == 'registry_mediator_revision':
                fields.insert(1, 'last_change_reason')
            else:
                fields.insert(1, 'change_reason')
        self.fieldsets[0][1]['fields'] = fields
        return self.fieldsets


@admin.register(Page)
class PageAdmin(SingleModelAdmin):
    pass
