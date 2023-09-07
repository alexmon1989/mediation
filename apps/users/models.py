from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import UserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    last_name = models.CharField("Прізвище", max_length=255, blank=True, null=True)
    first_name = models.CharField("Ім'я", max_length=255, blank=True, null=True)
    middle_name = models.CharField("По-батькові", max_length=255, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.email
