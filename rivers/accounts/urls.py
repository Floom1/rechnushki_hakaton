from django.urls import path
from .views import SignUpView, ChangePasswordView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('password_change/', ChangePasswordView.as_view(), name='password_change'),
]