# todo/models.py

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # link to user
    title = models.CharField(max_length=255)
    complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True)  # optional due date

    def is_overdue(self):
        if self.due_date:
            return timezone.now() > self.due_date
        return False

    def __str__(self):
        return self.title
