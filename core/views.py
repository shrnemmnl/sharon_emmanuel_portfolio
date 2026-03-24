from django.shortcuts import render
from .models import Profile, Experience, Project, Skill

def index(request):
    profile = Profile.objects.first()
    experiences = Experience.objects.all()
    projects = Project.objects.all()
    skills = Skill.objects.all()
    
    context = {
        'profile': profile,
        'experiences': experiences,
        'projects': projects,
        'skills': skills,
    }
    return render(request, 'index.html', context)
