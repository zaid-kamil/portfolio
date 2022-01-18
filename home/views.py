from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    skill_list = Skill.objects.all()
    project_list = Project.objects.all()
    ctx = {
        'skill_list': skill_list,
        'project_list': project_list,
        'title': 'Home',       
    }
    return render(request, 'home.html',context=ctx)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')