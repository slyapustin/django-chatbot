import time
from celery import shared_task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

channel_layer = get_channel_layer()

@shared_task
def add(x, y):
    async_to_sync(channel_layer.group_send)("calc", {"type": "calc.message", "message": '{} + {} = {}'.format(x, y, x + y)})    
