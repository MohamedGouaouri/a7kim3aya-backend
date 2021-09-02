from chat.models import Message
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
import json

from django.contrib.auth.models import User


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
        self.room_code = self.scope['url_route']['kwargs']['room_code']
        self.room_group_code = f'chat_{self.room_code}'

        # join room
        await self.channel_layer.group_add(
            self.room_group_code,
            self.channel_name
        )
        await self.accept()

        # TODO: Send to the user all the old messages

    async def disconnect(self, code):
        print("Consumer disconnected")
        await self.channel_layer.group_discard(
            self.room_group_code,
            self.channel_name
        )

    async def receive(self, text_data):
        message = json.loads(text_data.strip())
        print(message)
        await self.channel_layer.group_send(
            self.room_group_code,
            {
                'type': 'chat_message',
                'message': message,
            }
        )

        # TODO: Insert the message in the database
        # Since we are using async calls we need to wrap db calls with sync_to_async function
        sender = json.loads(message['sender'])
        receiver = json.loads(message['receiver'])
        message_from_id = sender['id']
        message_to_id = receiver['id']
        print(message_from_id, message_to_id)
        try:
            message_from = await sync_to_async(
                User.objects.get, thread_sensitive=True)(id=message_from_id)
            message_to = await sync_to_async(User.objects.get)(id=message_to_id)
            content = message['text']
            # insert int db
            await sync_to_async(Message.objects.create, thread_sensitive=True)(message_from=message_from, message_to=message_to, content=content)
        except User.DoesNotExist:
            print("User does not exist")
            pass

    async def chat_message(self, event):
        message = event['message']
        await self.send(text_data=json.dumps(message))
