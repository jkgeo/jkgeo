"""
recipes app urls
"""
from django.urls import path
from . import views

urlpatterns = [
	path('', views.recipeList, name='recipes'),
	path('<slug:recipe_slug>', views.recipeDetail, name='recipe_detail')
]