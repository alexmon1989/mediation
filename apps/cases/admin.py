from django.contrib import admin
from .models import Case


@admin.register(Case)
class EducationalCourseTypeAdmin(admin.ModelAdmin):
    ordering = ('pk',)
    list_display = ('case_number', 'mediator', 'created_at', 'updated_at')
    search_fields = ('case_number',)
    list_filter = ('mediator', )
    autocomplete_fields = ('mediator', )

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('mediator')
