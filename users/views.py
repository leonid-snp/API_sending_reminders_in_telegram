from rest_framework import generics
from rest_framework.permissions import AllowAny

from users.models import User
from users.serializers import UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """
    Класс представления создания пользователя.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer) -> None:
        """
        Переопределяем функцию для кеширования пароля.

        :param serializer:
        :return: None
        """
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserListAPIView(generics.ListAPIView):
    """
    Класс представления вывода списка пользователей.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateAPIView(generics.UpdateAPIView):
    """
    Класс представления обновления пользователя.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_update(self, serializer) -> None:
        """
        Переопределяем функцию для кеширования пароля.

        :param serializer:
        :return: None
        """
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """
    Класс представления детального просмотра пользователя.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDestroyAPIView(generics.DestroyAPIView):
    """
    Класс представления удаления пользователя.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
