from django.db import models

class Document(models.Model):
	name = models.CharField(max_length=128)
	type = models.CharField(max_length=64)
	added = models.DateTimeField(editable=False)
	modified = models.DateTimeField()
	models.FileField(upload_to='resume/files/%Y/%m/%d/')

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

	def __str__(self):
		return self.name


class Job(models.Model):
	title = models.CharField(max_length=128)
	employer = models.ForeignKey(Employer, on_delete=models.SET_NULL, null=True, blank=True)
	desc = models.TextField(null=True, blank=True)
	start = models.DateField()
	end = models.DateField(null=True, blank=True)
	current = models.BooleanField()

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


class Award(models.Model):
	order = models.IntegerField()
	name = models.CharField(max_length=255)
	desc = models.TextField()
	Job = models.ForeignKey(Job, on_delete=models.SET_NULL, null=True, blank=True)
	awarded = models.DateField()

	def __str__(self):
		return self.name


class SkillCategory(models.Model):
	name = models.CharField(max_length=255)

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
	category = models.ForeignKey(SkillCategory, on_delete=models.SET_NULL, null=True, blank=True)
	proficiency = models.IntegerField(
		choices=PROFICIENCY_CHOICES,
		null=True
	)
	since = models.DateField()

	def __str__(self):
		return self.name