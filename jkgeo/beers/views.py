from django.shortcuts import render
from .models import Beer

def beersList(request):
	beers = Beer.objects.all().order_by('added')
	context = {'beers': beers}	
	return render(request, 'beers/beers.html', context)