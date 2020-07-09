from django import forms
from .models import Beer, Brewery, Style, SubStyle

class BeerForm(forms.ModelForm):

	# customfield = forms.ModelChoiceField(queryset=)

	class Meta:
		model = Beer
		fields = ['name', 'brewery', 'style', 'sub_style', 'description', 'abv', 'rating', 'date_had', 'first_time', 'photo']
		#labels = {'name': 'Name'}
		widgets = {'date_had':forms.DateInput(attrs={'type': 'date'}), 'brewery': forms.Select(attrs={'class': 'ui add-beer fluid dropdown'}),
		    'style': forms.Select(attrs={'class': 'ui add-beer fluid dropdown'}), 'sub_style': forms.Select(attrs={'class': 'ui add-beer fluid dropdown'}),
		    'rating': forms.Select(attrs={'class': 'ui add-beer fluid dropdown'}), 'first_time': forms.NullBooleanSelect(attrs={'class': 'ui add-beer fluid dropdown'})
		}


class BreweryForm(forms.ModelForm):
    prefix = 'brewery'
    
    class Meta:
        model = Brewery
        fields = ['name', 'city', 'state']
        
        
class StyleForm(forms.ModelForm):
    prefix = 'style'
    
    class Meta:
        model = Style
        fields = ['name']
    
    def __init__(self, *args, **kwargs):
        super(StyleForm, self).__init__(*args, **kwargs)
        for key in self.fields:
            self.fields[key].required = False
        
        
class SubStyleForm(forms.ModelForm):
    prefix = 'sub-style'
    
    class Meta:
        model = SubStyle
        fields = ['name']
        
    def __init__(self, *args, **kwargs):
        super(SubStyleForm, self).__init__(*args, **kwargs)
        for key in self.fields:
            self.fields[key].required = False