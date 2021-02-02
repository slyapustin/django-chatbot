import json
from channels.generic.websocket import AsyncWebsocketConsumer

from . import tasks

COMMANDS = {
    'help': {
        'help': 'Display help message.',
    },
    'sum': {
        'args': 2,
        'help': 'Calculate sum of two integer arguments. Example: `sum 12 32`.',
        'task': 'add'
    },
    'status': {
        'args': 1,
        'help': 'Check website status. Example: `status twitter.com`.',
        'task': 'url_status'
    },
}

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        response_message = 'Please type `help` for the list of the commands.'
        message_parts = message.split()
        if message_parts:
            command = message_parts[0].lower()
            if command == 'help':
                response_message = 'List of the available commands:\n' + '\n'.join(
                    [f'{command} - {params["help"]} ' for command, params in COMMANDS.items()])
            elif command in COMMANDS:
                if len(message_parts[1:]) != COMMANDS[command]['args']:
                    response_message = f'Wrong arguments for the command `{command}`.'
                else:
                    getattr(tasks, COMMANDS[command]['task']).delay(self.channel_name, *message_parts[1:])
                    response_message = f'Command `{command}` received.'
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': response_message
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': f'[bot]: {message}'
        }))