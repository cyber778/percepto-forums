from threading import Thread
from django.db import models
from django.contrib.auth.models import User

class Content(models.Model):
    """ Base class for post/comment content """
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        abstract = True
        
    def __str__(self):
        return f'{self.author} - {self.body[:50]}'


class ContentThread(Content):
    pass


class Comment(Content):
    thread = models.ForeignKey(ContentThread, related_name="comments", on_delete=models.CASCADE)