from django.shortcuts import render
from .models import Projects
# Create your views here.

def home(request):
    context = {}
    return render(request, 'home.html', context)

def projectPage(request):
	all_projects = Projects.objects.all()
	context = {'projects': all_projects}
	return render(request, 'projects.html', context)