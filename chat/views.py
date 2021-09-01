from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import JsonResponse
from .models import UserResource
from .helpers import allow_cors_headers
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


def logout(request):
    # TODO Implement userlogout functionality
    pass


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
