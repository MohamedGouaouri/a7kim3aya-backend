from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name='index'),
    path("room/<str:room_code>/", room),
    path("auth/login/", auth),
    path("api/getusers/", get_all_users),
    path("api/get_chats/", get_chat_history)
]
