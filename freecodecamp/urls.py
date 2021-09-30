
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path("books/api/v1", include('products.urls')),
    path("api-auth/", include('rest_framework.urls')),
    path("api/v1/dj-rest-auth/", include("dj_rest_auth.urls")),
    #path("chat/", include('chat.urls')),
]
