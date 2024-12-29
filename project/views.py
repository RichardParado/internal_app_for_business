from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Project, Task
from django.contrib import messages
from .forms import TaskForm


# Create your views here.
@login_required
def task_view(request, project_id):
    brands = request.user.brands.all()
    project = get_object_or_404(Project, id=project_id, brand__in=brands)
    
    tasks = project.tasks.all().order_by('-created_at')
    context = {
        'tasks': tasks,
        'brands': brands,
        'project': project
    }
    return render(request, 'project/task-view.html', context)

@login_required
def task_create(request, project_id):
    brands = request.user.brands.all()
    project = get_object_or_404(Project, id=project_id, brand__in=brands)

    if request.method == 'POST':
        form = TaskForm(project.id, request.POST, request.FILES)

        if form.is_valid():
            task = form.save()

            messages.success(request, 'Task Created Successfully')
            return redirect('task-detail', project_id=project.id, task_id=task.id)
        else:
            messages.error(request, 'Error Creating Task')
    else:
        form = TaskForm(project_id=project.id)

    context = {
        'form': form,
        'brands': brands,
        'project': project
    }
    return render(request, 'project/task-form.html', context)

@login_required
def task_detail(request, project_id, task_id):
    brands = request.user.brands.all()

    task = get_object_or_404(Task, project__brand__in=brands, project_id=project_id, id=task_id)

    context = {
        'task': task,
        'brands': brands
    }
    return render(request, 'project/task-detail.html', context)

@login_required
def task_update(request, project_id, task_id):
    brands = request.user.brands.all()
    project = get_object_or_404(Project, id=project_id, brand__in=brands)


    task = get_object_or_404(Task, project__brand__in=brands, project_id=project_id, id=task_id)

    if request.method == 'POST':

        form = TaskForm(task.project.id, request.POST, request.FILES, instance=task)
        if form.is_valid():
            task = form.save()

            messages.success(request, 'Task Updated Successfully')
            return redirect('task-detail', project_id=task.project.id, task_id=task_id)
        else:
            messages.error(request, 'Error Updating Task')

    else:
        form = TaskForm(project_id=task.project.id, instance=task)

    current_attachment_url = task.attachment.url if task.attachment else None
    

    context = {
        'form': form,
        'brands': brands,
        'project': task.project,
        'current_attachment_url': current_attachment_url
    }
    return render(request, 'project/task-form.html', context)

@login_required
def task_delete(request, project_id, task_id):
    brands = request.user.brands.all()    
    task = get_object_or_404(Task, project__brand__in=brands, project_id=project_id, id=task_id)

    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Task Deleted Successfully')
        return redirect('task-view', project_id=task.project.id)
    
    context = {
        'task': task,
        'brands': brands
    }
    return render(request, 'project/task-delete.html', context)