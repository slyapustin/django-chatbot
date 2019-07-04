import time
from celery import shared_task

@shared_task
def add(x, y):
    time.sleep(0.3)
    return x + y
