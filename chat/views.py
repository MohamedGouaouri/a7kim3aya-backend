from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'chat/index.html', {})


def room(request, room_code):
    username = request.GET['username']
    # print(username)
    return render(request, 'chat/room.html', {'room_code': room_code, 'username': username})
