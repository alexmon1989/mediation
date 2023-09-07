from django.contrib import admin

from .models import Resource

@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    ordering = ('pk',)
    list_display = ('title', 'weight', 'enabled', 'created_at', 'updated_at')
    list_editable = ('weight', 'enabled')
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}
