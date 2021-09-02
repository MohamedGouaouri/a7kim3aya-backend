from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import JsonResponse, HttpRequest, response
from .models import Message, UserResource
from .helpers import allow_cors_headers
from asgiref.sync import sync_to_async
from django.db.models import Q
# Create your views here.


def index(request):
    return render(request, 'chat/index.html', {})


def room(request, room_code):
    username = request.GET['username']
    # print(username)
    return render(request, 'chat/room.html', {'room_code': room_code, 'username': username})


def register(request):
    # TODO: Implemenet user registration
    pass


@sync_to_async
def auth(request):
    username = request.GET['username']
    password = request.GET['password']
    user = authenticate(username=username, password=password)
    if user:

        user_resources = UserResource.objects.filter(user_id=user).first()
        response = JsonResponse({'loged_in': True,
                                 'user': {'id': user.pk, 'name': user.get_username()},
                                 'imageUrl': user_resources.imageUrl,
                                 'roomPartialCode': user_resources.roomPartialCode
                                 }, safe=False)
        response = allow_cors_headers(response)
        return response
    else:
        response = JsonResponse({'loged_in': False}, safe=False)
        response = allow_cors_headers(response)
        return response


@sync_to_async
def logout(request):
    # TODO Implement userlogout functionality
    pass


@sync_to_async
def get_all_users(request):
    usersdb = User.objects.all()
    users = []
    for userdb in usersdb:

        user_resources = UserResource.objects.filter(user_id=userdb).first()
        users.append({
            'id': userdb.pk,
            'name': userdb.username,
            'imageUrl': user_resources.imageUrl,
            'isOnline': userdb.is_authenticated,
            'roomPartialCode': user_resources.roomPartialCode
        })

    response = JsonResponse(users, safe=False)
    response = allow_cors_headers(response)
    return response


@sync_to_async
def get_chat_history(request: HttpRequest):
    messages_from = request.GET['from']
    messages_to = request.GET['to']
    chat_historydb = Message.objects.filter(
        Q(message_from=messages_from, message_to=messages_to) | Q(message_from=messages_to, message_to=messages_from)).order_by('-at')

    chat_history = []
    for message in chat_historydb:
        if message.message_from.id == messages_from:
            chat_history.append({
                'id': message.id,
                'sender': {'id': message.message_from.id},
                'receiver': {'id': message.message_to.id},
                'text': message.content,
                'time': message.at
            })
        else:
            chat_history.append({
                'id': message.id,
                'sender': {'id': message.message_to.id},
                'receiver': {'id': message.message_from.id},
                'text': message.content,
                'time': message.at
            })
    response = JsonResponse(chat_history, safe=False)
    response = allow_cors_headers(response)
    return response
