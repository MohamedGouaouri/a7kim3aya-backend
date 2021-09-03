from django.urls import path
from .views import *

urlpatterns = [
    path("auth/login/", auth),
    path("api/getusers/", get_all_users),
    path("api/get_chats/", get_chat_history)
]
