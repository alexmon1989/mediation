from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Resource


@admin.register(Resource)
class ResourceAdmin(TranslationAdmin):
    ordering = ('pk',)
    list_display = ('pk', 'title', 'weight', 'enabled', 'created_at', 'updated_at')
    list_editable = ('weight', 'enabled')
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}
