import datetime

from rest_framework.validators import ValidationError


class FieldValidation:
    """
    Проверяет на одновременное заполнение полей
    associated_habit и prize.
    """

    def __init__(self, obj: object) -> None:
        self.obj = obj

    def __call__(self, obj: dict) -> None:
        if obj.get('associated_habit') and obj.get('prize'):
            raise ValidationError(
                'Нельзя заполнять одновременно и `связанную привычку` и `вознаграждение`'
            )


class TimeValidation:
    """
    Проверяет время выполнения привычки
    не должно превышать 120 секунд.
    """

    def __init__(self, field: str) -> None:
        self.obj = field

    def __call__(self, field: dict) -> None:
        if field.get('lead_time'):
            if field.get('lead_time') > datetime.time(0, 2):
                raise ValidationError(
                    'Время выполнения не должно превышать 120 секунд'
                )


class AssociatedValidation:
    """
    Проверяет связанную привычку на признак `приятная`.
    """

    def __init__(self, field: str) -> None:
        self.field = field

    def __call__(self, field: dict) -> None:
        if field.get('associated_habit'):
            if not field.get('associated_habit').nice_habit:
                raise ValidationError(
                    'Связанная привычка может быть только с признаком `приятная`'
                )


class NiceHabitValidation:
    """
    Проверяет приятную привычку на соответствие критериям:
    не может содержать связанную привычку.
    не может иметь вознаграждение.
    """
    def __init__(self, obj: object) -> None:
        self.obj = obj

    def __call__(self, obj: dict) -> None:
        if obj.get('nice_habit') and obj.get('associated_habit') or obj.get('prize'):
            raise ValidationError(
                'У приятной привычки не может быть `связанной привычки` или `вознаграждения`'
            )
