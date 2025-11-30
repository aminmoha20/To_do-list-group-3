# todo/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Main list page (named 'list' for redirects and links)
    path('', views.index, name='list'), 
    
    # URL to update a specific task
    path('update/<int:pk>/', views.updateTask, name='update_task'), 
    
    # URL to delete a specific task
    path('delete/<int:pk>/', views.deleteTask, name='delete'),
]