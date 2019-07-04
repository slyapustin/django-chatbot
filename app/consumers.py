from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
from .tasks import add


class CalcConsumer(WebsocketConsumer):
    def connect(self):
        self.group_name = 'calc'

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

        try:
            x, y = message.split('+')
            x = int(x)
            y = int(y)
            add.delay(x, y)
            message = 'Calculating {} ...'.format(message)
        except:
            message = 'Unsupported format'

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
            {
                'type': 'calc_message',
                'message': message
            }
        )

    # Receive message from calc
    def calc_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))
