from django.urls import path
from . import views

app_name = 'task'
urlpatterns = [
    path('', views.index, name='index'),
    path('createTask/', views.createTask, name='createTask'),
    path('deleteTask/<int:task_id>', views.deleteTask, name='deleteTask'),
]