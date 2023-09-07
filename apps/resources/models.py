from django.db import models
from django.urls import reverse

from ckeditor_uploader.fields import RichTextUploadingField

from apps.common.models import TimeStampModel


class Resource(TimeStampModel):
    """Модель ресурса."""
    title = models.CharField('Заголовок', max_length=255)
    slug = models.SlugField('Мітка для URL', max_length=127, unique=True)
    content = RichTextUploadingField('Текст')
    weight = models.PositiveSmallIntegerField(
        'Вага',
        default=0,
        help_text='Чим більша вага, тим нижче ресурс буде у меню'
    )
    enabled = models.BooleanField('Відображати на сайті', default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("resources:detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Ресурс'
        verbose_name_plural = 'Ресурси'
        db_table = 'recources'
        ordering = ('weight', 'created_at', 'title')
