from django.contrib import admin
from .models import Cuisine, Ingredient, Recipe, Quantity, UnitsOfMeasure, Step, Note, Equipment

admin.site.register(Cuisine)
admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(Quantity)
admin.site.register(UnitsOfMeasure)
admin.site.register(Step)
admin.site.register(Note)
admin.site.register(Equipment)