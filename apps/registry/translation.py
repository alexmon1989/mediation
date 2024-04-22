from modeltranslation.translator import translator, TranslationOptions
from .models import Page, Mediator, MediatorEducation


class PageTranslationOptions(TranslationOptions):
    fields = ('content',)


class MediatorTranslationOptions(TranslationOptions):
    fields = ('last_name', 'first_name', 'middle_name', 'additional_info')


class MediatorEducationTranslationOptions(TranslationOptions):
    fields = ('qualification', )


translator.register(Page, PageTranslationOptions)
translator.register(Mediator, MediatorTranslationOptions)
translator.register(MediatorEducation, MediatorEducationTranslationOptions)
