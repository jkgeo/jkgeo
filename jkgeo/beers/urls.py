"""
beers app urls
"""
from django.urls import path
from . import views

urlpatterns = [
	path('', views.beersList, name='beers'),
	path('add', views.addBeer, name='add-beer')
]