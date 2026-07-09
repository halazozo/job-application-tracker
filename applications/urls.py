from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('add/', views.add_application, name='add_application'),
    path('edit/<int:pk>/', views.edit_application, name='edit_application'),
    path('delete/<int:pk>/', views.delete_application, name='delete_application'),
]