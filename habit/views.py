from django.db.models import Q
from rest_framework import generics

from habit.models import Habit
from habit.permissions import IsAuthor
from habit.serializers import HabitSerializer


class HabitCreateAPIView(generics.CreateAPIView):
    """
    Класс представления создания привычки.
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    def perform_create(self, serializer) -> None:
        """
        Переопределяем функцию чтобы
        присвоить привычке текущего пользователя.

        :param serializer:
        :return: None
        """
        user = self.request.user
        habit = serializer.save(author=user)
        habit.save()


class HabitListAPIView(generics.ListAPIView):
    """
    Класс представления вывода списка привычек.
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    def get_queryset(self) -> None:
        """
        Переопределяем функцию для фильтрации привычек
        только на просмотр публичных привычек,

        приватные привычки могут смотреть только
        создавшие эту привычку пользователи.

        :return: None
        """
        user = self.request.user
        queryset = Habit.objects.filter(Q(public_habit=True) | Q(author=user))
        return queryset


class HabitUpdateAPIView(generics.UpdateAPIView):
    """
    Класс представления обновления привычки.
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (IsAuthor,)


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """
    Класс представления детального просмотра привычки.
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (IsAuthor,)


class HabitDestroyAPIView(generics.DestroyAPIView):
    """
    Класс представления удаления привычки.
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (IsAuthor,)
