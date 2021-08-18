from django.urls import path, include

from rest_framework import routers
from .views import BloggerViewSet, BlogViewSet, atomic_create_blogger


router = routers.DefaultRouter()
router.register(r'blogs', BlogViewSet)
router.register(r'bloggers', BloggerViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path("api/add_blogger/", atomic_create_blogger),
]
