from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Beer, Brewery, Style, SubStyle
from .forms import BeerForm, BreweryForm, StyleForm, SubStyleForm
from django.contrib.auth.decorators import login_required

def beersList(request):
  beers = Beer.objects.all().order_by('-date_had')
  context = {'beers': beers}
  return render(request, 'beers/beers.html', context)

@login_required
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
    brewery = request.session.get('brewery', None)
    style = request.session.get('style', None)
    sub_style = request.session.get('sub_style', None)
    
    form = BeerForm(initial={'brewery': brewery, 'style': style, 'sub_style': sub_style})
    
    return render(request, 'beers/add_beer.html', {'beerform':form})
    

@login_required
def addBrewery(request):
  breweries = Brewery.objects.all()
  if request.method == 'POST':
    selected = int(request.POST.get('select-brewery', 0))

    if selected > 0:
        request.session['brewery'] = selected
        return redirect('add-style')
    else:
        filled_form = BreweryForm(request.POST)
        if filled_form.is_valid():
          new_brewery = filled_form.save()
          request.session['brewery'] = new_brewery.pk
          return redirect('add-style')
        else:
          note = 'please try again'
          
    
  else:
    form = BreweryForm()
    return render(request, 'beers/add_brewery.html', {'breweries': breweries, 'breweryform':form})


@login_required
def addStyle(request):
  styles = Style.objects.all()
  substyles = SubStyle.objects.all()
  if request.method == 'POST':
    selected_style = int(request.POST.get('select-style', 0))
    selected_sub_style = int(request.POST.get('select-sub-style', 0))
    
    if selected_style > 0:
        request.session['style'] = selected_style
    elif selected_style == 0:
        style_form = StyleForm(request.POST, prefix='style')
        if style_form.is_valid():
          new_style = style_form.save()
          request.session['style'] = new_style.pk
          
    if selected_sub_style > 0:
        request.session['sub_style'] = selected_sub_style
    elif selected_sub_style == 0:
        sub_style_form = SubStyleForm(request.POST, prefix='sub-style')
        if sub_style_form.is_valid():
          new_sub_style = sub_style_form.save()
          request.session['sub_style'] = new_sub_style.pk
        
    if selected_style > -1:
        return redirect('add-beer')
    else:
        note = 'please try again'
        new_styleform = StyleForm()
        new_substyleform = SubStyleForm()
        return render(request, 'beers/add_style.html', {'note': note, 'styles': styles, 'substyles': substyles, 'styleform':new_styleform, 'substyleform': new_substyleform})
      
        
  else:
    styleform = StyleForm()
    substyleform = SubStyleForm()
    return render(request, 'beers/add_style.html', {'styles': styles, 'substyles': substyles, 'styleform':styleform, 'substyleform': substyleform})
    