from django.contrib import admin
from django.db import models
from django.forms import Textarea

from singlemodeladmin import SingleModelAdmin
from modeltranslation.admin import TranslationAdmin

from .models import Phone, Email, Contact


class PhoneInline(admin.StackedInline):
    model = Phone
    extra = 1


class EmailInline(admin.StackedInline):
    model = Email
    extra = 1


@admin.register(Contact)
class ContactAdmin(SingleModelAdmin, TranslationAdmin):
    ordering = ('pk',)
    inlines = [
        PhoneInline,
        EmailInline,
    ]
    formfield_overrides = {
        models.TextField: {'widget': Textarea(
            attrs={'rows': 2})},
    }
