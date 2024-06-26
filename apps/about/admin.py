from django.contrib import admin

from singlemodeladmin import SingleModelAdmin
from modeltranslation.admin import TranslationAdmin

from .models import Page


@admin.register(Page)
class PageAdmin(SingleModelAdmin, TranslationAdmin):
    pass
