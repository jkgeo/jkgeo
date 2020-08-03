from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Project(models.Model):
	PRIVATE = 0
	PUBLIC = 1

	PERSONAL = 0
	PROFESSIONAL = 1

	PROJECT_VISIBILITY_CHOICES = [
	    (PRIVATE, 'Private'),
	    (PUBLIC, 'Public')
	]

	PROJECT_TYPE_CHOICES = [
		(PERSONAL, 'Personal'),
		(PROFESSIONAL, 'Professional')
	]

	name = models.CharField(max_length=255)
	type = models.IntegerField(
		choices=PROJECT_TYPE_CHOICES
	)
	visibility = models.IntegerField(
		choices=PROJECT_VISIBILITY_CHOICES,
		null=True,
		blank=True
	)
	description = models.TextField(null=True, blank=True)
	thumbnail = models.ImageField(upload_to='project_thumbs', null=True, blank=True)
	slug = models.SlugField(blank=True)

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Project, self).save(*args, **kwargs)


class UserProfile(models.Model):
	# This line is required. Links UserProfile to a User model instance.
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	# The additional attributes we wish to include.
	picture = models.ImageField(upload_to='profile_images', blank=True)
	

	def __str__(self):
		return self.user.username