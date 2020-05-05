from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
	PRIVATE = 0
	PUBLIC = 1

	PROJECT_VISIBILITY_CHOICES = [
	    (PRIVATE, 'Private'),
	    (PUBLIC, 'Public')
	]

	name = models.CharField(max_length=255)
	type = models.CharField(max_length=255)
	visibility = models.IntegerField(
		choices=PROJECT_VISIBILITY_CHOICES,
		null=True
	)
	description = models.TextField()

	def __str__(self):
		return self.name

class UserProfile(models.Model):
	# This line is required. Links UserProfile to a User model instance.
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	# The additional attributes we wish to include.
	picture = models.ImageField(upload_to='profile_images', blank=True)
	
	def __str__(self):
		return self.user.username