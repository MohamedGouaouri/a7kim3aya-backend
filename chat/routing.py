from django.urls import path
from . import consumers

websockets_urlpatterns = [
    path('ws/<str:peer_code>/', consumers.ChatConsumer.as_asgi())
]
