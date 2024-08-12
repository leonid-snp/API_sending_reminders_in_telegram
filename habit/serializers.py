from rest_framework import serializers

from habit.models import Habit
from habit.validators import (AssociatedValidation, FieldValidation,
                              NiceHabitValidation, TimeValidation)


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [
            FieldValidation(fields),
            TimeValidation(field='lead_time'),
            NiceHabitValidation(fields),
            AssociatedValidation(field='associated_habit')
        ]
