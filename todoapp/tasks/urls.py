from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.list, name='list'),
    path('create/', views.create_task, name='create_task'),
    path('delete/<int:uid>', views.delete, name='delete_task'),
    path('modify/<int:uid>', views.modify, name='modify_task'),
    path('test/', views.test, name='test'),
    path('details/<int:pk>', views.TaskDetail, name='details'),

]
