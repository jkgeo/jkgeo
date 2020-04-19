from django.db import models
from django.utils import timezone

class SubStyle(models.Model):
	name = models.CharField(max_length=64)

	def __str__(self):
		return self.name

class Style(models.Model):
	name = models.CharField(max_length=32)
	sub_style = models.ManyToManyField(SubStyle, blank=True)

	def __str__(self):
		return self.name

class Brewery(models.Model):
	name = models.CharField(max_length=128)
	city = models.CharField(max_length=32)
	state= models.CharField(max_length=32)

	def __str__(self):
		return self.name

class Beer(models.Model):
	OK = 1
	PRETTY_GOOD = 2
	GREAT = 3

	BEER_RATING_CHOICES = [
	    (OK, 'OK'),
	    (PRETTY_GOOD, 'Pretty Good'),
	    (GREAT, 'Great'),
	]

	name = models.CharField(max_length=128)
	brewery = models.ForeignKey(Brewery, on_delete=models.SET_NULL, null=True, blank=True)
	style = models.ForeignKey(Style, on_delete=models.SET_NULL, null=True, blank=True)
	sub_style = models.ForeignKey(SubStyle, on_delete=models.SET_NULL, null=True, blank=True)
	description = models.TextField(null=True, blank=True)
	abv = models.FloatField(null=True)
	rating = models.IntegerField(
		choices=BEER_RATING_CHOICES,
		null=True
	)
	added = models.DateTimeField(editable=False)
	modified = models.DateTimeField()
	first_time = models.BooleanField(null=True)
	photo = models.ImageField(upload_to='beers')

	def save(self, *args, **kwargs):
		''' On save, update timestamps '''
		if not self.id:
			self.added = timezone.now()
		self.modified = timezone.now()
		return super(Beer, self).save(*args, **kwargs)

	def __str__(self):
		return self.name