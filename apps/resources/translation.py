from modeltranslation.translator import translator, TranslationOptions
from .models import Resource


class ResourceTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


translator.register(Resource, ResourceTranslationOptions)
