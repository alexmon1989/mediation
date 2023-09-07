from django.contrib import admin

from .models import (EducationalInstitution, EducationalCourse, Language, Region, Speciality, WorkFormat,
                     Specialization, ProfessionalDirections)


@admin.register(EducationalInstitution)
class EducationalInstitutionTypeAdmin(admin.ModelAdmin):
    ordering = ('pk',)
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title',)


@admin.register(EducationalCourse)
class EducationalCourseTypeAdmin(admin.ModelAdmin):
    ordering = ('pk',)
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title',)


@admin.register(Language)
class LanguageTypeAdmin(admin.ModelAdmin):
    ordering = ('pk',)
    list_display = ('title', 'weight', 'created_at', 'updated_at')
    list_editable = ('weight',)
    search_fields = ('title',)


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    ordering = ('pk',)
    list_display = ('title', 'weight', 'created_at', 'updated_at')
    list_editable = ('weight',)
    search_fields = ('title',)


@admin.register(Speciality)
class SpecialityAdmin(admin.ModelAdmin):
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
class WorkFormatAdmin(admin.ModelAdmin):
    ordering = ('pk',)
    list_display = ('title', 'weight', 'created_at', 'updated_at')
    list_editable = ('weight',)
    search_fields = ('title',)


@admin.register(ProfessionalDirections)
class ProfessionalDirectionsAdmin(admin.ModelAdmin):
    ordering = ('pk',)
    list_display = ('title', 'weight', 'created_at', 'updated_at')
    list_editable = ('weight',)
    search_fields = ('title',)
