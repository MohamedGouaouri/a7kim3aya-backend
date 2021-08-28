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
        print("Consumer connected")

    async def connect(self):

        self.room_code = self.scope['url_route']['kwargs']['room_code']
        self.room_group_code = f'chat_{self.room_code}'

        # join room
        await self.channel_layer.group_add(
            self.room_group_code,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.room_group_code,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        username = data['username']
        room = data['room']
        await self.channel_layer.group_send(
            self.room_group_code,
            {
                'type': 'chat_message',
                'message': message,
                'username': username
            }
        )
        # self.send(text_data=json.dumps({
        #     'message': message,
        #     'username': username
        # }))
        print(data)

    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username
        }))
