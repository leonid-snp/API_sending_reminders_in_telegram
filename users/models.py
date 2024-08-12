from django.contrib.auth.models import AbstractUser
from django.db import models

from config.settings import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True,
        max_length=150,
        verbose_name='E-mail',
        help_text='Укажите E-mail'
    )
    password = models.CharField(
        max_length=150,
        verbose_name='Пароль',
        help_text='Укажите пароль'
    )
    tg_chat_id = models.CharField(
        unique=True,
        verbose_name='ID чата телеграмма',
        help_text='Укажите ID чата телеграмма',
        default=None,
        **NULLABLE
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
