from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Tasks(models.Model):
    task = models.CharField(max_length=100)
    posted_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.task

    def get_absolute_url(self):
        return reverse(viewname="user-home")
