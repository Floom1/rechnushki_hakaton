from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.homepage_view, name='home'),
    path('about/', views.about_view, name='about'),
]