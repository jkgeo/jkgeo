"""
beers app urls
"""
from django.urls import path
from . import views

urlpatterns = [
	path('', views.beersList, name='beers'),
	path('add-beer', views.addBeer, name='add-beer'),
	path('add-brewery', views.addBrewery, name='add-brewery'),
	path('add-style', views.addStyle, name='add-style')
]