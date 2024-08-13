from celery import shared_task

from habit.services import get_habit


@shared_task
def add_task() -> None:
    """
    Добавляем периодическую задачу.

    :return: None
    """
    get_habit()
