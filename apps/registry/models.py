from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils.functional import cached_property
from django.urls import reverse

from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField

from apps.common.models import TimeStampModel
from apps.classifiers.models import (EducationalInstitution, EducationalCourse, Speciality, Language, WorkFormat,
                                     Region, Specialization, ProfessionalDirections)
from .dataclasses import MediatorTraining as MediatorTrainingDataClass

from typing import List


# Дозволені розширення файлів сертифікату про навчання
CERTIFICATES_EXT_ALLOWED = (
    'pdf',
    'jpg',
    'jpeg',
    'png',
    'gif'
)

CHANGE_REASON_CHOICES = (
    ('', '----'),
    ("tech", "Технічні виправлення"),
    ("biblio", "Зміни в бібліографії"),
)


class Mediator(TimeStampModel):
    """Модель медіатора."""
    application_number = models.CharField("Номер заяви", max_length=255)
    application_date = models.DateField("Дата заяви")
    last_name = models.CharField("Прізвище", max_length=255)
    first_name = models.CharField("Ім'я", max_length=255)
    middle_name = models.CharField("По-батькові", max_length=255, blank=True)
    photo = models.ImageField(
        'Фото',
        upload_to='mediators/%Y/%m/%d',
        null=True,
        blank=True,
        help_text='Розмір зображення - 600*900 пікселей. Якщо зображення має інший розмір, то воно буде приведено до розміру 600*900 автоматично.'
    )
    educations = models.ManyToManyField(EducationalInstitution, through='MediatorEducation', blank=True)
    languages = models.ManyToManyField(Language, blank=True, verbose_name='Мова')
    specialities = models.ManyToManyField(Speciality, blank=True, verbose_name='Спеціальність')
    work_format = models.ForeignKey(WorkFormat, on_delete=models.CASCADE, null=True, blank=True,
                                    verbose_name='Формат роботи')
    regions = models.ManyToManyField(Region, blank=True, verbose_name='Регіон роботи')
    trainings = models.ManyToManyField(EducationalCourse, through='MediatorTraining', blank=True,
                                       related_name='basic_training')
    specializations = models.ManyToManyField(Specialization, blank=True, verbose_name='Спеціалізація')
    professional_directions = models.ManyToManyField(ProfessionalDirections,
                                                     blank=True,
                                                     through='MediatorProfessionalDirections',
                                                     verbose_name='Спеціалізація медіатора '
                                                                  'у сфері інтелектуальної власності, сферах бізнесу')

    # Контактна інформація
    address = models.TextField('Адреса для листування', max_length=512, null=True, blank=True)
    email = models.EmailField('Електронна адреса', null=True, blank=True)
    phones = models.CharField('Номери телефонів', max_length=255, null=True, blank=True)

    # Додаткова інформація
    additional_info = RichTextField('Додаткова інформація', max_length=16384, null=True, blank=True)

    active = models.BooleanField('Активний', default=False, help_text='Визначає чи буде особу опубліковано на сайті')
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='Оновлено')
    last_change_reason = models.CharField('Причина змін', null=True, blank=True, choices=CHANGE_REASON_CHOICES,
                                           max_length=6)

    def __str__(self):
        res = f"{self.last_name} {self.first_name}"
        if self.middle_name:
            res = f"{res} {self.middle_name}"
        return res

    def get_absolute_url(self):
        return reverse('registry:detail', args=[self.pk])

    @property
    def specializations_titles(self) -> List[str]:
        """Повертає список зі спеціалізаціями медіатора."""
        return self.specializations.values_list('title', flat=True)

    @property
    def specialities_titles(self) -> List[str]:
        """Повертає список зі спеціальностями медіатора."""
        return self.specialities.values_list('title', flat=True)

    @property
    def professional_directions_titles(self) -> List[str]:
        """Повертає список із професійними напрямкками медіатора."""
        res = self.mediatorprofessionaldirections_set.order_by('-weight').select_related('professional_direction')
        return [item.professional_direction.title for item in res]

    @property
    def regions_titles(self) -> List[str]:
        """Повертає список із регіонами роботи медіатора."""
        return self.regions.values_list('title', flat=True)

    @property
    def languages_titles(self) -> List[str]:
        """Повертає список із регіонами роботи медіатора."""
        return self.languages.values_list('title', flat=True)

    @property
    def educations_titles(self) -> List[str]:
        """Повертає список із освітами медіатора."""
        res = []
        educations = self.mediatoreducation_set.order_by('pk', 'year_from').select_related('education_institution')
        for item in educations:
            years = []
            years_str = ''
            qualification = ''
            if item.year_from:
                years.append(str(item.year_from))
            if item.year_to:
                years.append(str(item.year_to))
            if years:
                years_str = ' - '.join(years)
                years_str = f" ({years_str})"
            if item.qualification:
                qualification = f" ({item.qualification})"
            res.append(f"{item.education_institution.title}{years_str}{qualification}")
        return res

    @cached_property
    def trainings_detailed(self) -> List[MediatorTrainingDataClass]:
        res = []
        for item in self.mediatortraining_set.select_related(
                'education_institution', 'education_course'
        ).order_by('year', 'pk'):
            res.append(
                MediatorTrainingDataClass(
                    type_code=item.training_type,
                    institution_title=item.education_institution.title,
                    education_course_title=item.education_course.title,
                    hours=item.hours,
                    year=item.year,
                    certificate_url=item.certificate.url if item.certificate else ''
                )
            )
        return res

    @cached_property
    def basic_trainings(self) -> List[MediatorTrainingDataClass]:
        return list(filter(lambda x: x.type_code == 'BASIC', self.trainings_detailed))

    @cached_property
    def spec_trainings(self) -> List[MediatorTrainingDataClass]:
        return list(filter(lambda x: x.type_code == 'SPEC', self.trainings_detailed))

    @cached_property
    def additional_trainings(self) -> List[MediatorTrainingDataClass]:
        return list(filter(lambda x: x.type_code == 'ADDITIONAL', self.trainings_detailed))

    @property
    def has_contact_info(self) -> bool:
        return any([
            self.address,
            self.email,
            self.phones,
        ])

    class Meta:
        verbose_name = 'Медіатор'
        verbose_name_plural = 'Медіатори'
        db_table = 'mediators'


class MediatorProfessionalDirections(TimeStampModel):
    """Модель професійних напрямків медіатора."""
    mediator = models.ForeignKey(Mediator, on_delete=models.CASCADE)
    professional_direction = models.ForeignKey(ProfessionalDirections,
                                               on_delete=models.CASCADE,
                                               verbose_name='Професійний напрямок')
    weight = models.PositiveIntegerField(default=0,
                                         verbose_name='Вага',
                                         help_text='Чим більша вага, тим далі елемент буде у списку значень поля')

    class Meta:
        verbose_name = 'Професійний напрямок медіатора'
        verbose_name_plural = 'Професійні напрямки медіатора'
        db_table = 'mediators_professional_directions'

    def __str__(self):
        return self.professional_direction.title


class MediatorEducation(TimeStampModel):
    """Модель освіти медіатора."""
    mediator = models.ForeignKey(Mediator, on_delete=models.CASCADE)
    education_institution = models.ForeignKey(EducationalInstitution, on_delete=models.CASCADE,
                                              verbose_name='Освітній заклад')
    year_from = models.PositiveIntegerField('Рік з', null=True, blank=True)
    year_to = models.PositiveIntegerField('Рік по', null=True, blank=True)
    qualification = models.CharField('Кваліфікація', blank=True, default='')
    certificate = models.FileField(
        'Файл сертифікату',
        upload_to='certificates/%Y/%m/%d/',
        validators=[FileExtensionValidator(allowed_extensions=CERTIFICATES_EXT_ALLOWED)],
        help_text=f"Дозволені розширення файлу: {', '.join(CERTIFICATES_EXT_ALLOWED)}",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Освіта'
        verbose_name_plural = 'Освіта'
        db_table = 'mediators_educations'

    def __str__(self):
        return f"{self.education_institution.title} ({self.year_from} - {self.year_to})"


class MediatorTraining(TimeStampModel):
    """Модель базової підготовки медіатора."""

    class TrainingType(models.TextChoices):
        BASIC = 'BASIC', 'Базова підготовка'
        SPEC = 'SPEC', 'Спеціалізована підготовка'
        ADDITIONAL = 'ADDITIONAL', 'Підвищення професійного рівня'

    training_type = models.CharField(
        max_length=10,
        choices=TrainingType.choices,
        verbose_name='Тип підготовки'
    )
    mediator = models.ForeignKey(Mediator, on_delete=models.CASCADE)
    education_institution = models.ForeignKey(EducationalInstitution, on_delete=models.CASCADE,
                                              verbose_name='Освітній заклад')
    education_course = models.ForeignKey(EducationalCourse, on_delete=models.CASCADE,
                                              verbose_name='Назва курсу')
    hours = models.PositiveIntegerField('Кількість годин', null=True, blank=True)
    year = models.PositiveIntegerField('Рік', null=True, blank=True)
    certificate = models.FileField(
        'Файл сертифікату',
        upload_to='certificates/%Y/%m/%d/',
        validators=[FileExtensionValidator(allowed_extensions=CERTIFICATES_EXT_ALLOWED)],
        help_text=f"Дозволені розширення файлу: {', '.join(CERTIFICATES_EXT_ALLOWED)}",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Підготовка медіатора'
        verbose_name_plural = 'Підготовка медіатора'
        db_table = 'mediators_trainings'

    def __str__(self):
        return f"{self.education_institution.title} - {self.education_course.title} ({self.year})"


class Page(TimeStampModel):
    """Модель сторінки списку медіаторів."""
    content = RichTextUploadingField('Текст')
    show = models.BooleanField('Відображати текст для користувачів веб-сайту')

    class Meta:
        verbose_name = 'Сторінка списку медіаторів'
        verbose_name_plural = 'Сторінка списку медіаторів'
        db_table = 'mediators_page'
