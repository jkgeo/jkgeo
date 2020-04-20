from django.db import models

class Employer(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.title

class Job(models.Model):
	title = models.CharField(max_length=128)
	employer = models.ForeignKey(Employer, on_delete=models.SET_NULL, null=True, blank=True)

	def __str__(self):
		return self.title