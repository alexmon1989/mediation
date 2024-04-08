from django.contrib import admin

from modeltranslation.admin import TranslationAdmin

from .models import (EducationalInstitution, EducationalCourse, Language, Region, Speciality, WorkFormat,
                     Specialization, ProfessionalDirections)


@admin.register(EducationalInstitution)
class EducationalInstitutionTypeAdmin(TranslationAdmin):
    ordering = ('pk',)
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title',)


@admin.register(EducationalCourse)
class EducationalCourseTypeAdmin(TranslationAdmin):
    ordering = ('pk',)
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title',)


@admin.register(Language)
class LanguageTypeAdmin(TranslationAdmin):
    ordering = ('pk',)
    list_display = ('title', 'weight', 'created_at', 'updated_at')
    list_editable = ('weight',)
    search_fields = ('title',)


@admin.register(Region)
class RegionAdmin(TranslationAdmin):
    ordering = ('pk',)
    list_display = ('title', 'weight', 'created_at', 'updated_at')
    list_editable = ('weight',)
    search_fields = ('title',)


@admin.register(Speciality)
class SpecialityAdmin(TranslationAdmin):
    ordering = ('pk',)
    list_display = ('title', 'weight', 'created_at', 'updated_at')
    list_editable = ('weight',)
    search_fields = ('title',)


@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    ordering = ('pk',)
    list_display = ('title', 'weight', 'created_at', 'updated_at')
    list_editable = ('weight',)
    search_fields = ('title',)


@admin.register(WorkFormat)
class WorkFormatAdmin(TranslationAdmin):
    ordering = ('pk',)
    list_display = ('title', 'weight', 'created_at', 'updated_at')
    list_editable = ('weight',)
    search_fields = ('title',)


@admin.register(ProfessionalDirections)
class ProfessionalDirectionsAdmin(TranslationAdmin):
    ordering = ('pk',)
    list_display = ('title', 'weight', 'created_at', 'updated_at')
    list_editable = ('weight',)
    search_fields = ('title',)
