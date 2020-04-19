from django.db import models

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