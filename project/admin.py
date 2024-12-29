from django.contrib import admin
from .models import Project, Task

# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'description', 'created_at', 'updated_at')
    search_fields = ('name', 'brand')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'project', 'assignee', 'due_date', 'status', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('status', 'due_date', 'assignee', 'project')