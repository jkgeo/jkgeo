from django.shortcuts import render
from .models import Job, Accomplishment, Employer, Document, \
Resource, Degree, Skill, SkillCategory, Service, Presentation, Publication


def resume(request):
	jobs = Job.objects.all().order_by('-start')
	employers = Employer.objects.all()
	documents = Document.objects.all()
	degrees = Degree.objects.all().order_by('-awarded')
	service = Service.objects.all()
	publications = Publication.objects.all()
	presentations = Presentation.objects.all()
	
	employment = []
	
	for job in jobs:
		job_dict = {}
		job_dict['job'] = job
		# employer_dict = {}
		# employer_dict['name'] = job.employer.name
		# employer_dict['city'] = job.employer.city
		# employer_dict['state'] = job.employer.state
		job_dict['employer'] = job.employer
		job_dict['logo'] = job.employer.logo
		job_dict['accomplishments'] = []
		accs = Accomplishment.objects.filter(job=job).order_by('order')
		resources = Resource.objects.filter(job=job).order_by('order')
		for acc in accs:
			job_dict['accomplishments'].append(acc.desc)

		resource_list = []
		for resource in resources:
			resource_dict = {}
			if resource.active:
				resource_dict['name'] = resource.name
				resource_dict['link'] = resource.link
			if resource.desc:
				resource_dict['desc'] = resource.desc
			resource_list.append(resource_dict)
		
		job_dict['resources'] = resource_list
		employment.append(job_dict)

	skills = []
	skill_categories = SkillCategory.objects.all().order_by('id')
	for category in skill_categories:
		skill_list = {}
		skill_list['category'] = category
		skill_list['skills'] = Skill.objects.filter(category=category)
		skills.append(skill_list)

	context = {
		'jobs': employment,
		'degrees': degrees,
		'docs': documents,
		'skills': skills,
		'service': service,
		'pubs': publications,
		'presies': presentations
	}

	return render(request, 'resume/resume.html', context)