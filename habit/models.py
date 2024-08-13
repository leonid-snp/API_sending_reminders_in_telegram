from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone

from config.settings import NULLABLE
from users.models import User


class Habit(models.Model):
    """
    Класс модели привычки.
    """
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор привычки',
        help_text='Укажите автора привычки',
        **NULLABLE
    )
    location = models.CharField(
        max_length=150,
        verbose_name='Место',
        help_text='Укажите место выполнения',
    )
    time = models.TimeField(
        default=timezone.now,
        verbose_name='Время',
        help_text='Укажите время выполнения',
    )
    action = models.CharField(
        verbose_name='Действие',
        help_text='Укажите действие привычки',
    )
    nice_habit = models.BooleanField(
        verbose_name='Признак привычки',
        help_text='Укажите признак приятной привычки'
    )
    associated_habit = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        verbose_name='Связанная привычка',
        help_text='Укажите связанную привычку',
        **NULLABLE
    )
    periodicity = models.PositiveSmallIntegerField(
        default=7,
        validators=[MinValueValidator(1), MaxValueValidator(7)],
        verbose_name='Периодичность',
        help_text='Укажите периодичность выполнения'
    )
    prize = models.CharField(
        max_length=150,
        verbose_name='Вознаграждение',
        help_text='Укажите вознаграждение',
        **NULLABLE
    )
    lead_time = models.TimeField(
        default='00:02:00',
        verbose_name='Время на выполнение',
        help_text='Укажите время на выполнение привычки'
    )
    public_habit = models.BooleanField(
        verbose_name='Признак публичности',
        help_text='Укажите признак публичности'
    )

    def __str__(self):
        return self.action

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
