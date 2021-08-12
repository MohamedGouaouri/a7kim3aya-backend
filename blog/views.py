from django.shortcuts import render

from .models import Blog, Blogger
# Create your views here.


def raw_sql():
    # Suppose we want to get all blogs of of bloger_id = 1
    blogs = Blog.objects.raw(
        "SELECT id, bloger_id FROM blog WHERE blogger_id = 1")
    if len(blogs) > 0:
        return blogs
    return None
