from django.urls import path
from .views import *

urlpatterns = [
    path("", home),
    path("about/", about),
    path("details/", product_details),
    path("create/", create_product),
    path("show/", getAllProducts),
    path('show/<int:pid>/', getProductById, name='show-by-id'),
    path("delete/<int:pid>", deleteById),
]
