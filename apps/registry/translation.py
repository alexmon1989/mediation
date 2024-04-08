from modeltranslation.translator import translator, TranslationOptions
from .models import Page, Mediator


class PageTranslationOptions(TranslationOptions):
    fields = ('content',)


class MediatorTranslationOptions(TranslationOptions):
    fields = ('last_name', 'first_name', 'middle_name', 'additional_info')


translator.register(Page, PageTranslationOptions)
translator.register(Mediator, MediatorTranslationOptions)
