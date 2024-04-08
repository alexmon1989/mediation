from modeltranslation.translator import translator, TranslationOptions
from .models import (EducationalInstitution, EducationalCourse, Language, Region, WorkFormat, Speciality,
                     Specialization, ProfessionalDirections)


class EducationalInstitutionTranslationOptions(TranslationOptions):
    fields = ('title', )


class EducationalCourseTranslationOptions(TranslationOptions):
    fields = ('title', )


class LanguageTranslationOptions(TranslationOptions):
    fields = ('title', )


class RegionTranslationOptions(TranslationOptions):
    fields = ('title', )


class WorkFormatTranslationOptions(TranslationOptions):
    fields = ('title', )


class SpecialityTranslationOptions(TranslationOptions):
    fields = ('title', )


class SpecializationTranslationOptions(TranslationOptions):
    fields = ('title', )


class ProfessionalDirectionsTranslationOptions(TranslationOptions):
    fields = ('title', )


translator.register(EducationalInstitution, EducationalInstitutionTranslationOptions)
translator.register(EducationalCourse, EducationalCourseTranslationOptions)
translator.register(Language, LanguageTranslationOptions)
translator.register(Region, RegionTranslationOptions)
translator.register(WorkFormat, WorkFormatTranslationOptions)
translator.register(Speciality, SpecialityTranslationOptions)
translator.register(Specialization, SpecializationTranslationOptions)
translator.register(ProfessionalDirections, ProfessionalDirectionsTranslationOptions)
