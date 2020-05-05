from django.db import models
from django.utils import timezone


class Document(models.Model):
	name = models.CharField(max_length=128)
	type = models.CharField(max_length=64)
	added = models.DateTimeField(editable=False)
	modified = models.DateTimeField()
	file = models.FileField(upload_to='resume/files/%Y/%m/%d/', null=True)

	def save(self, *args, **kwargs):
		''' On save, update timestamps '''
		if not self.id:
			self.added = timezone.now()
		self.modified = timezone.now()
		return super(Document, self).save(*args, **kwargs)

	def __str__(self):
		return self.name


class Employer(models.Model):
	name = models.CharField(max_length=255)
	city = models.CharField(max_length=128)
	state = models.CharField(max_length=2)
	desc = models.TextField(null=True, blank=True)
	logo = models.ImageField(upload_to='employer_logos', null=True, blank=True)

	def __str__(self):
		return self.name


class Job(models.Model):
	title = models.CharField(max_length=128)
	employer = models.ForeignKey(Employer, on_delete=models.SET_NULL, null=True, blank=True)
	desc = models.TextField(null=True, blank=True)
	start = models.DateField()
	end = models.DateField(null=True, blank=True)
	current = models.BooleanField()
	relevant = models.BooleanField(null=True, blank=True, default=True)

	def __str__(self):
		return self.title


class Service(models.Model):
	title = models.CharField(max_length=128)
	employer = models.ForeignKey(Employer, on_delete=models.SET_NULL, null=True, blank=True)
	desc = models.TextField(null=True, blank=True)
	start = models.DateField()
	end = models.DateField(null=True, blank=True)
	current = models.BooleanField()

	def __str__(self):
		return self.title


class Accomplishment(models.Model):
	order = models.IntegerField()
	desc = models.CharField(max_length=255)
	job = models.ForeignKey(Job, on_delete=models.CASCADE, null=True, blank=True)
	service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, blank=True)

	def __str__(self):
		identifier = f'{self.job.title} - {self.order}'
		return identifier


class Award(models.Model):
	order = models.IntegerField()
	name = models.CharField(max_length=255)
	desc = models.TextField()
	job = models.ForeignKey(Job, on_delete=models.SET_NULL, null=True, blank=True)
	awarded = models.DateField()

	def __str__(self):
		return self.name


class Resource(models.Model):
	order = models.IntegerField()
	name = models.CharField(max_length=255)
	desc = models.TextField(null=True, blank=True)
	link = models.URLField(max_length=255, null=True, blank=True)
	job = models.ForeignKey(Job, on_delete=models.SET_NULL, null=True, blank=True)
	service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, blank=True)
	active = models.BooleanField()

	def __str__(self):
		return self.name


class SkillCategory(models.Model):
	name = models.CharField(max_length=255)
	icon = models.CharField(max_length=255, null=True, blank=True)

	def __str__(self):
		return self.name


class Skill(models.Model):
	BEGINNER = 1
	INTERMEDIATE = 2
	EXPERT = 3

	PROFICIENCY_CHOICES = [
	    (BEGINNER, 'Beginner'),
	    (INTERMEDIATE, 'Intermediate'),
	    (EXPERT, 'Expert'),
	]

	name = models.CharField(max_length=128)
	category = models.ManyToManyField(SkillCategory)
	proficiency = models.IntegerField(
		choices=PROFICIENCY_CHOICES,
		null=True
	)
	since = models.DateField(null=True, blank=True)

	def __str__(self):
		return self.name


class University(models.Model):
	name = models.CharField(max_length=255)
	city = models.CharField(max_length=128)
	state = models.CharField(max_length=2)
	desc = models.TextField(null=True, blank=True)
	logo = models.ImageField(upload_to='school_logos', null=True, blank=True)

	def __str__(self):
		return self.name


class Degree(models.Model):
	title = models.CharField(max_length=128)
	type = models.CharField(max_length=10, null=True, blank=True)
	major = models.CharField(max_length=128, null=True, blank=True)
	concentration = models.CharField(max_length=255, null=True, blank=True)
	uni = models.ForeignKey(University, on_delete=models.SET_NULL, null=True, blank=True)
	desc = models.TextField(null=True, blank=True)
	awarded = models.DateField(null=True, blank=True)

	def __str__(self):
		return self.title


class Presentation(models.Model):
	name = models.CharField(max_length=255)
	type = models.CharField(max_length=64)
	citation = models.TextField()
	date = models.DateField()

	def __str__(self):
		return self.name

class Publication(models.Model):
	name = models.CharField(max_length=255)
	citation = models.TextField()
	date = models.DateField()
	refereed = models.BooleanField()

	def __str__(self):
		return self.name