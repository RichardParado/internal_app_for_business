from django.urls import path
from . import views

urlpatterns = [
    path('<str:project_id>/', views.task_view, name='task-view'),
    path('<str:project_id>/task/new/', views.task_create, name='task-create'),
    path('<str:project_id>/task/<str:task_id>/', views.task_detail, name='task-detail'),
    path('<str:project_id>/task/<str:task_id>/update/', views.task_update, name='task-update'),
    path('<str:project_id>/task/<str:task_id>/delete/', views.task_delete, name='task-delete'),
]