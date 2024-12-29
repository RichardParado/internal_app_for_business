from django import forms
from .models import Task
from django.contrib.auth.models import User


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'assignee', 'due_date', 'status', 'priority', 'attachment']
        widgets = {
            'assignee': forms.Select(attrs={'class': 'form-control mb-2'}),
            'name': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'description': forms.Textarea(attrs={'class': 'form-control mb-2'}),
            'due_date': forms.DateInput(attrs={'class': 'form-control mb-2', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-control mb-2'}),
            'priority': forms.Select(attrs={'class': 'form-control mb-2'}),
            'attachment': forms.FileInput(attrs={'class': 'form-control mb-2'})
        }

    def __init__(self, project_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.project_id = project_id

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.project_id = self.project_id
        if commit:
            instance.save()
        return instance