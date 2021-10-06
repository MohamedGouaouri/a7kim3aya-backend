from products.models import Product
from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import ProductSerializer


def home(request):

    return render(request=request, template_name="home.html")


# show all products
class ProductAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CreateProductAPIView(generics.CreateAPIView):
    #permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProductSerializer
