from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
from .tasks import add, url_status


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.group_name = 'chat'

        # Join calc
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        if message.startswith('sum'):
            try:
                _, x, y = message.split()
                x = int(x)
                y = int(y)
                add.delay(x, y)
            except:
                pass
        elif message.startswith('status'):
            _, url = message.split()
            url_status(url)
        else:
            message = 'Unsupported format'

            # Send message to room group
            async_to_sync(self.channel_layer.group_send)(
                self.group_name,
                {
                    'type': 'chat_message',
                    'message': message
                }
            )

    def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': f'bot> {message}'
        }))
