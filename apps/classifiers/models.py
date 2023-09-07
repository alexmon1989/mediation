from django.db import models
from apps.common.models import TimeStampModel


class EducationalInstitution(TimeStampModel):
    """Модель освітнього закладу."""
    title = models.CharField('Назва', max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Освітній заклад'
        verbose_name_plural = 'Освітній заклад'
        db_table = 'cl_educational_institutions'
        ordering = ('title',)


class EducationalCourse(TimeStampModel):
    """Модель навчального курса."""
    title = models.CharField('Назва', max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Навчальний курс'
        verbose_name_plural = 'Навчальні курси'
        db_table = 'cl_educational_courses'
        ordering = ('title',)


class Language(TimeStampModel):
    """Модель мови медіатора."""
    title = models.CharField('Значення', max_length=255)
    weight = models.PositiveSmallIntegerField(
        'Вага',
        default=0,
        help_text='Чим більша вага, тим далі елемент буде у списку значень поля'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Мова'
        verbose_name_plural = 'Мови'
        db_table = 'cl_languages'
        ordering = ('weight', 'created_at',)


class Region(TimeStampModel):
    """Модель регіона роботи."""
    title = models.CharField('Назва', max_length=255)
    weight = models.PositiveSmallIntegerField(
        'Вага',
        default=1,
        help_text='Чим більша вага, тим далі елемент буде у списку значень поля'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Регіон роботи'
        verbose_name_plural = 'Регіони роботи'
        db_table = 'cl_regions'
        ordering = ('weight', 'created_at',)


class WorkFormat(TimeStampModel):
    """Модель формата роботи."""
    title = models.CharField('Значення', max_length=255)
    weight = models.PositiveSmallIntegerField(
        'Вага',
        default=0,
        help_text='Чим більша вага, тим далі елемент буде у списку значень поля'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Формат роботи'
        verbose_name_plural = 'Формати роботи'
        db_table = 'cl_work_formats'
        ordering = ('weight', 'created_at',)


class Speciality(TimeStampModel):
    """Модель спеціальності медіатора."""
    title = models.CharField('Назва', max_length=255)
    weight = models.PositiveSmallIntegerField(
        'Вага',
        default=1,
        help_text='Чим більша вага, тим далі елемент буде у списку значень поля'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Спеціальність'
        verbose_name_plural = 'Спеціальності'
        db_table = 'cl_specialities'
        ordering = ('weight', 'created_at',)


class Specialization(TimeStampModel):
    """Модель спеціалізації медіатора."""
    title = models.CharField('Назва', max_length=255)
    weight = models.PositiveSmallIntegerField(
        'Вага',
        default=1,
        help_text='Чим більша вага, тим далі елемент буде у списку значень поля'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Спеціалізація'
        verbose_name_plural = 'Спеціалізації'
        db_table = 'cl_specializations'
        ordering = ('weight', 'created_at',)


class ProfessionalDirections(TimeStampModel):
    """Модель професійного напрямку медіатора."""
    title = models.CharField('Назва', max_length=255)
    weight = models.PositiveSmallIntegerField(
        'Вага',
        default=0,
        help_text='Чим більша вага, тим далі елемент буде у списку значень поля'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Професійний напрямок'
        verbose_name_plural = 'Професійні напрямки'
        db_table = 'cl_professional_directions'
        ordering = ('weight', 'created_at',)
