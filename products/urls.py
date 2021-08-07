from django.urls import path
from .views import home, about, product_details, create_product, show

urlpatterns = [
    path("", home),
    path("about/", about),
    path("details/", product_details),
    path("create/", create_product),
    path('show/<int:pid>/', show, name='show')
]
