from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),

    path(
        'activate/<uidb64>/<token>/',
        views.activate_account,
        name='activate_account'
    ),

    path(
        'password-reset/',
        auth_views.PasswordResetView.as_view(
            template_name='applications/password_reset_form.html',
            email_template_name='applications/password_reset_email.html',
            subject_template_name='applications/password_reset_subject.txt',
            success_url=reverse_lazy('custom_password_reset_done')
        ),
        name='custom_password_reset'
    ),

    path(
        'password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='applications/password_reset_done.html'
        ),
        name='custom_password_reset_done'
    ),

    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='applications/password_reset_confirm.html',
            success_url=reverse_lazy('custom_password_reset_complete')
        ),
        name='custom_password_reset_confirm'
    ),

    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='applications/password_reset_complete.html'
        ),
        name='custom_password_reset_complete'
    ),

    path('add/', views.add_application, name='add_application'),
    path('edit/<int:pk>/', views.edit_application, name='edit_application'),
    path('delete/<int:pk>/', views.delete_application, name='delete_application'),
]