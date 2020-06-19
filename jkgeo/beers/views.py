from django.shortcuts import render
from .models import Beer
from .forms import BeerForm

def beersList(request):
	beers = Beer.objects.all().order_by('-date_had')
	context = {'beers': beers}	
	return render(request, 'beers/beers.html', context)

def addBeer(request):
	if request.method == 'POST':
		filled_form = BeerForm(request.POST, request.FILES)
		if filled_form.is_valid():
			filled_form.save()
			name = filled_form.cleaned_data['name']
			note = f'Nice! {name} sounds good.'
		else:
			note = 'please try again'
		new_form = BeerForm()
		return render(request, 'beers/add_beer.html', {'beerform':new_form, 'note':note})
	else:
		form = BeerForm()
		return render(request, 'beers/add_beer.html', {'beerform':form})