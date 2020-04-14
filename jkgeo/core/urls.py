"""
core app urls
"""
from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('projects/', views.projectPage, name='projects')
]