from django.db import models

class Projects(models.Model):
	name = models.CharField(max_length=255)
	type = models.CharField(max_length=255)
	description = models.TextField()
