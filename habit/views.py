from django.db.models import Q
from rest_framework import generics

from habit.models import Habit
from habit.permissions import IsAuthor
from habit.serializers import HabitSerializer
from habit.services import get_chat_id_user


class HabitCreateAPIView(generics.CreateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        user = self.request.user
        habit = serializer.save(author=user)
        get_chat_id_user(user.email)
        habit.save()


class HabitListAPIView(generics.ListAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Habit.objects.filter(Q(public_habit=True) | Q(author=user))
        return queryset


class HabitUpdateAPIView(generics.UpdateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (IsAuthor,)


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (IsAuthor,)


class HabitDestroyAPIView(generics.DestroyAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (IsAuthor,)
