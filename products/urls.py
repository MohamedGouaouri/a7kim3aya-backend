from django.urls import path, re_path
from .views import *

urlpatterns = [
    path("", home, name='home'),
    path("list/", ProductAPIView.as_view()),
    path("create/", CreateProductAPIView.as_view()),
]
