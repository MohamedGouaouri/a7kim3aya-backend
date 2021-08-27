from django.urls import path, re_path
from .views import *

urlpatterns = [
    path("", home, name='home'),
    path("about/", about),
    path("details/", product_details),
    path("create/", create_product),
    path("show/", getAllProducts),
    path('show/<int:pid>/', getProductById, name='show-by-id'),
    path("delete/<int:pid>/", deleteById),
    path("http/", http_view),
    path("upload/", upload),
    path("all/", AllProductsView.as_view()),
    re_path(r"^\d\w+py$", re_view)

]
