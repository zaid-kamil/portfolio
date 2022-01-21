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
        'hactive':'class=active',     
    }
    return render(request, 'home.html',context=ctx)

def about(request):
    ctx = {
         'aactive':'class=active',  
    }
    return render(request, 'about.html',context=ctx)

def contact(request):
    ctx={
         'cactive':'class=active',  
    }
    return render(request, 'contact.html',context=ctx)