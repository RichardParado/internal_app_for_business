from django.urls import path
from . import views

urlpatterns = [
    path('', views.leave_list, name='leave-list'),
    path('apply', views.apply_leave, name='apply-leave'),
    path('approve/<str:application_id>/', views.approve_leave, name='approve-leave'),
    path('reject/<str:application_id>/', views.reject_leave, name='reject-leave'),
    path('detail/<str:application_id>/', views.leave_detail, name='leave-detail')

]