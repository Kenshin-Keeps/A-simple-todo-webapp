from django import forms
from .models import Tasks

class AddTask(forms.ModelForm):
    task = forms.CharField(max_length=100)
    class Meta:
        model = Tasks
        fields = ["task"]