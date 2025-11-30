# todo/models.py

from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    # Renamed 'complete' to 'completed' for clarity (ensure you check your template matches this)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Displays the task title in the Django Admin
        return self.title