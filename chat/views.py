import json
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import JsonResponse, HttpRequest
from asgiref.sync import sync_to_async
from .models import Message, UserResource
from .helpers import allow_cors_headers
from django.db.models import Q
from django.core import serializers


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
    print(request.user.is_authenticated)
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
    first_point = request.GET['from']
    second_point = request.GET['to']
    chat_historydb = Message.objects.filter(
        Q(message_from=first_point, message_to=second_point) | Q(message_from=second_point, message_to=first_point)).order_by('-at')

    chat_history = []
    for message in chat_historydb:
        chat_history.append({
            'id': message.id,
            'message_from': {'id': message.message_from_id},
            'message_to': {'id': message.message_to_id},
            'content': message.content,
            'time': message.at
        })

    response = JsonResponse(chat_history, safe=False)
    response = allow_cors_headers(response)
    return response
