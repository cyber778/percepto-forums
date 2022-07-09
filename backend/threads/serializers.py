from concurrent.futures import thread
from django.contrib.auth.models import User

from .models import ContentThread, Comment
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'is_staff']
        

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    author = UserSerializer(read_only=True, default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Comment
        fields = ['id', 'url', 'body', 'author', 'created', 'thread']
        

class ContentThreadSerializer(serializers.HyperlinkedModelSerializer):
    comments = CommentSerializer(many=True, required=False)
    author = UserSerializer(read_only=True, default=serializers.CurrentUserDefault())
    
    class Meta:
        model = ContentThread
        fields = ['id', 'url', 'body', 'author', 'created', 'comments']