import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

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

class ChatConsumer(WebsocketConsumer):
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        response_message = 'Please type `help` for the list of the commands.'
        message_parts = message.split()
        if message_parts:
            command = message_parts[0].lower()
            if command == 'help':
                response_message = 'List of the available commands:\n' + '\n'.join([f'{command} - {params["help"]} ' for command, params in COMMANDS.items()])
            elif command in COMMANDS:
                if len(message_parts[1:]) != COMMANDS[command]['args']:
                    response_message = f'Wrong arguments for the command `{command}`.'
                else:
                    getattr(tasks, COMMANDS[command]['task']).delay(self.channel_name, *message_parts[1:])
                    response_message = f'Command `{command}` received.'
        
        async_to_sync(self.channel_layer.send)(
                self.channel_name,
                {
                    'type': 'chat_message',
                    'message': response_message
                }
            )

    def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': f'[bot]: {message}'
        }))
