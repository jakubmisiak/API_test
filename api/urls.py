from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='first'),
    path('task-list/', views.taskList, name='task-list'),
    path('task/<int:id>', views.taskDetail, name='task'),
    path('task-create/', views.taskCreate, name='create'),
    path('task-update/<int:id>', views.taskUpdate, name='update'),
    path('task-delete/<int:id>', views.taskDelete, name = 'delete'),
]