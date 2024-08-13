from django.contrib import admin

from habit.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    """
    Класс регистрации модели привычек в админ.
    """
    list_display = ('id', 'author', 'time', 'nice_habit', 'periodicity', 'public_habit')
    list_filter = ('id', 'author', 'time', 'nice_habit', 'periodicity', 'public_habit')
    search_fields = ('author', 'time', 'nice_habit', 'periodicity', 'public_habit')
