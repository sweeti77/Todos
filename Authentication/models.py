from django.db import models
from django.contrib.auth.models import User

# Create your models here

class Todo(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField(blank=True)
    important = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title
