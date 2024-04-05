from modeltranslation.translator import translator, TranslationOptions
from .models import Contact


class ContactTranslationOptions(TranslationOptions):
    fields = ('address', 'work_hours')


translator.register(Contact, ContactTranslationOptions)
