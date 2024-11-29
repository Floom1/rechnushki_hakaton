from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.accounts_view, name='home'),
]