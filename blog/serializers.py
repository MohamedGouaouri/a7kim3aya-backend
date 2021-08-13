
from .models import Blog, Blogger

from rest_framework import serializers


class BloggerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blogger
        fields = ['name', 'email']


class BlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blog
        fields = ['name', 'body', 'tagline', 'blogger']
