from django.shortcuts import render

from .models import Blog, Blogger


from rest_framework import viewsets
from .serializers import BloggerSerializer, BlogSerializer


def raw_sql():
    # Suppose we want to get all blogs of of bloger_id = 1
    blogs = Blog.objects.raw(
        "SELECT id, bloger_id FROM blog WHERE blogger_id = 1")
    if len(blogs) > 0:
        return blogs
    return None


class BloggerViewSet(viewsets.ModelViewSet):
    queryset = Blogger.objects.all()
    serializer_class = BloggerSerializer


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
