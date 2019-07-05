import time

import requests
from asgiref.sync import async_to_sync
from celery import shared_task
from channels.layers import get_channel_layer
from django.core.cache import cache

channel_layer = get_channel_layer()

@shared_task
def add(channel_name, x, y):
    message = '{}+{}={}'.format(x, y, int(x) + int(y))
    async_to_sync(channel_layer.send)(channel_name, {"type": "chat.message", "message": message})


@shared_task
def url_status(channel_name, url):
    if not url.startswith('http'):
        url = f'https://{url}'

    status = cache.get(url)
    if not status:
        try:
            r = requests.get(url, timeout=10)
            status = r.status_code
            cache.set(url, status, 60*60)
        except requests.exceptions.RequestException:
            status = 'Not available'

    message = f'{url} status is {status}'
    async_to_sync(channel_layer.send)(channel_name, {"type": "chat.message", "message": message})
