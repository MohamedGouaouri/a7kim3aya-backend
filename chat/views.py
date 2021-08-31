from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import JsonResponse
from .models import UserResource
# Create your views here.


def index(request):
    return render(request, 'chat/index.html', {})


def room(request, room_code):
    username = request.GET['username']
    # print(username)
    return render(request, 'chat/room.html', {'room_code': room_code, 'username': username})


def auth(request):
    username = request.GET['username']
    password = request.GET['password']
    user = authenticate(username=username, password=password)
    if user:

        user_resources = UserResource.objects.filter(user_id=user).first()
        return JsonResponse({'loged_in': True,
                             'user': {'id': user.pk, 'name': user.get_username()},
                             'imageUrl': user_resources.imageUrl})
    else:
        return JsonResponse({'loged_in': False})
