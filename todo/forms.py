# todo/forms.py

from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    # This widget removes the default label and adds a placeholder text
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add a new task...'}))
    
    class Meta:
        model = Task
        fields = ['title', 'completed']
        # We only display the 'title' field for the creation form
        # We need 'completed' for the update form
        exclude = ['completed']