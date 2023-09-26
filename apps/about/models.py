from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from apps.common.models import TimeStampModel


class Page(TimeStampModel):
    title = models.CharField('Заголовок', max_length=255)
    content = RichTextUploadingField('Текст')

    def __str__(self):
        return 'Зміст сторінки'

    class Meta:
        verbose_name = 'Зміст сторінки'
        verbose_name_plural = 'Зміст сторінки'
        db_table = 'about'
