from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
import json


# A consumer simply does the following :
# - accepts connections,
# - receives data
# - send data
# - close connection

class ChatConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def connect(self):

        print("Consumer connected")
        self.peer_code = self.scope['url_route']['kwargs']['peer_code']
        self.peer_group_code = f'chat_{self.peer_code}'

        # join room
        await self.channel_layer.group_add(
            self.peer_group_code,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, code):
        print("Consumer disconnected")
        await self.channel_layer.group_discard(
            self.peer_group_code,
            self.channel_name
        )

    async def receive(self, text_data):
        message = json.loads(text_data.strip())
        print(text_data.strip())
        await self.channel_layer.group_send(
            self.peer_group_code,
            {
                'type': 'chat_message',
                'message': message,
            }
        )

    async def chat_message(self, event):
        message = event['message']
        await self.send(text_data=json.dumps(message))
