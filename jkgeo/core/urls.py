"""
core app urls
"""
from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('projects/', views.projectPage, name='projects'),
	path('accounts/', include('django.contrib.auth.urls')),
# 	path('register/', views.register, name='register'),
# 	path('login/', views.login, name='login')
]