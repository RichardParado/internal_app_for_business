from django.db import models
from dashboard.models import Brand
from leave_tracker.models import Employee

STATUSES = (
    ('open', 'Open'),
    ('in progress', 'In Progress'),
    ('closed', 'Closed')
)

PRIORITIES = (
    (1, 'Urgent'),
    (2, 'High'),
    (3, 'Normal'),
    (4, 'Low')
)

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='projects')
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    assignee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name='tasks')
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=100, choices=STATUSES, default='Open')
    priority = models.IntegerField(choices=PRIORITIES, default=4)
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name