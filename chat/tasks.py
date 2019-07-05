import time

import requests
from asgiref.sync import async_to_sync
from celery import shared_task
from channels.layers import get_channel_layer
from django.core.cache import cache

channel_layer = get_channel_layer()

@shared_task
def add(x, y):
    message = '{} + {} = {}'.format(x, y, x + y)
    async_to_sync(channel_layer.group_send)("chat", {"type": "chat.message", "message": message})


@shared_task
def url_status(url):
    status = cache.get(url)
    if not status:
        # Cache in Redis
        r = requests.get(url)
        status = r.status_code
        cache.set(url, status, 60*60)

    message = 'URL {} status is {}'.format(url, status)
    async_to_sync(channel_layer.group_send)("chat", {"type": "chat.message", "message": message})
