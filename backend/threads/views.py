from django.shortcuts import render
from django.contrib.auth.models import User

from .models import Comment, ContentThread
from rest_framework import viewsets
from rest_framework import permissions

from .serializers import ContentThreadSerializer, CommentSerializer, UserSerializer
from .utils import IsAdminOrSelf


class ContentThreadViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Threads to be viewed or edited (by creators or admins).
    """
    queryset = ContentThread.objects.all()
    serializer_class = ContentThreadSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        
    def perform_destroy(self, instance):
        print(self.request.user.is_staff, instance.author, self.request.user)
        if self.request.user.is_staff or instance.author == self.request.user:
            return super().perform_destroy(instance)


class CommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows comments to be viewed or edited (by creators or admins).
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        
    def perform_destroy(self, instance):
        print(self.request.user.is_staff, instance.author, self.request.user)
        if self.request.user.is_staff or instance.author == self.request.user:
            return super().perform_destroy(instance)
        

    
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
