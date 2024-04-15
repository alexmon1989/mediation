from django.contrib import admin
from django.db import models
from django.forms import Textarea
from django.urls import resolve

from reversion.admin import VersionAdmin
from singlemodeladmin import SingleModelAdmin
from modeltranslation.admin import TranslationAdmin

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


class ProfessionalDirectionsInline(admin.TabularInline):
    model = Mediator.professional_directions.through
    extra = 1
    verbose_name_plural = 'Професійні напрямки'
    autocomplete_fields = (
        'professional_direction',
    )

    def get_queryset(self, request):
        return super().get_queryset(request).order_by('-weight')


@admin.register(Mediator)
class MediatorAdmin(VersionAdmin, TranslationAdmin):
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
        ProfessionalDirectionsInline,
        EducationInline,
        TrainingInline,
    ]
    autocomplete_fields = (
        'specialities',
        'specializations',
        'languages',
        'regions',
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
            "last_name_uk",
            "first_name_uk",
            "middle_name_uk",
            "last_name_en",
            "first_name_en",
            "middle_name_en",
            "photo",
            "languages",
            "specialities",
            "specializations",
            "work_format",
            "regions",
            "additional_info_uk",
            "additional_info_en",
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
class PageAdmin(SingleModelAdmin, TranslationAdmin):
    pass
