import requests
from config import settings
from habit.models import Habit
from users.models import User


def send_telegram_message(chat_id: str, message: str) -> None:
    """
    Отправляем сообщение в телеграмме.

    :param chat_id: (str) чат-id пользователя
    :param message: (str) сообщение в телеграмм
    :return: None
    """
    params = {
        'text': message,
        'chat_id': chat_id
    }
    requests.get(f'{settings.TG_API_URL}{settings.TG_API_TOKEN}/sendMessage', params=params)


def get_chat_id_user(email: str) -> str:
    """
    Получаем телеграм чат-id пользователя.

    :param email: (str) почта пользователя
    :return: (str) чат-id пользователя
    """
    user = User.objects.get(email=email)
    return user.tg_chat_id

# def get_message_habit():
#     message = Habit.objects.filter()


def check_periodicity(habit: object) -> None:
    habit.get('periodicity')


def get_habit() -> None:
    habit = Habit.objects.all()
    check_periodicity(habit)
