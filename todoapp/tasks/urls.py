from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='list'),
    path('create/', views.create_task, name='create_task'),
    path('delete/<int:uid>', views.delete, name='delete_task'),
    path('modify/<int:uid>', views.modify, name='modify_task'),
]
