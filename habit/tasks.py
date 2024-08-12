from celery import shared_task

from habit.services import get_chat_id_user


@shared_task
def add_task():
    print('Hello')
