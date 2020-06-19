from django import forms
from .models import Beer

class BeerForm(forms.ModelForm):

	# customfield = forms.ModelChoiceField(queryset=)

	class Meta:
		model = Beer
		fields = ['name', 'brewery', 'style', 'sub_style', 'description', 'abv', 'rating', 'date_had', 'first_time', 'photo']
		#labels = {'name': 'Name'}
		#widgets = {'name':forms.Textarea}
