"""
league app urls
"""
from django.urls import path
from . import views

urlpatterns = [
	path('', views.league, name='league'),
]