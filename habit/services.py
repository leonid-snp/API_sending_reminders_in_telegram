from datetime import datetime

import requests

from config import settings
from habit.models import Habit


def send_telegram_message(chat_id: str, message: str) -> None:
    """
    Отправляем сообщение в телеграмме.

    :param chat_id: (str) чат-id пользователя
    :param message: (str) сообщение в телеграмм
    :return: None
    """
    params = {
        'chat_id': chat_id,
        'text': message,
    }
    requests.post(f'{settings.TG_API_URL}{settings.TG_API_TOKEN}/sendMessage', params=params)


def collecting_message(habit: list) -> None:
    """
    Собираем сообщение для телеграмма.

    :param habit: (list) привычки
    :return: None
    """
    total_data = datetime.now().strftime('%H:%M')
    for item in habit:
        message = f'Привет не забудь сегодня в {item.time.strftime('%H:%M')} {item.action}'
        if item.time.strftime('%H:%M') == total_data:
            send_telegram_message(item.author.tg_chat_id, message)


def get_habit() -> None:
    """
    Получаем привычки у которых пользователь
    имеет телеграмм chat_id.

    :return: None
    """
    habit = Habit.objects.all()
    habit_is_use_tg = [item for item in habit if item.author.tg_chat_id]
    collecting_message(habit_is_use_tg)
