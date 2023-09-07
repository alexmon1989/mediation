from django.db import models
from apps.common.models import TimeStampModel


class Contact(TimeStampModel):
    address = models.TextField('Адреса', blank=True, null=True)
    work_hours = models.TextField('Режим роботи', blank=True, null=True)
    form_email = models.EmailField('E-Mail форми зв\'язку', max_length=255)

    def __str__(self):
        return 'Контактні дані'

    class Meta:
        verbose_name = 'Контактні дані'
        verbose_name_plural = 'Контактні дані'
        db_table = 'contacts'


class Phone(TimeStampModel):
    value = models.CharField('Телефон', max_length=255)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефони'


class Email(TimeStampModel):
    email = models.EmailField('E-Mail', max_length=255)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'E-Mail'
        verbose_name_plural = 'E-Mail'
