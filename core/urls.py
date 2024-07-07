from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('tasks/', views.TaskListView.as_view(), name='task_list'),
    path('tasks/create/', views.TaskCreateView.as_view(), name='task_create'),
    re_path(r'^tasks/(?P<pk>\d+)/update/$', views.TaskUpdateView.as_view(), name='task_update'),
    re_path(r'^tasks/(?P<pk>\d+)/delete/$', views.TaskDeleteView.as_view(), name='task_delete'),
]