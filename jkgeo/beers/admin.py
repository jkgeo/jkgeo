from django.contrib import admin
from .models import Beer, Style, SubStyle, Brewery

admin.site.register(Beer)
admin.site.register(Style)
admin.site.register(Brewery)
admin.site.register(SubStyle)