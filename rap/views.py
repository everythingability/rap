import requests
import os

from django.http import HttpResponse
from django.contrib.auth.models import Group, User
from django.contrib.auth.decorators  import login_required
from django.shortcuts import render, redirect

from django.contrib import messages
from .models import Project, GTRCategory, HECategory, HEResearchArea, Person
from .forms import ProjectForm

def home(request):
    return render(request, "home.html", {} )

# Create your views here.
def dashboard(request):

    projects = Project.objects.all()
    hecategories = HECategory.objects.all()
    herearchareas = HEResearchArea.objects.all()
    gtrCategories  = GTRCategory.objects.all()


    context = {'hecategories':hecategories,
               'herearchareas':herearchareas,
               'gtrCategories':gtrCategories,
               'projects':projects
                }


    return render(request, "projects/dashboard.html", context )

def projects(request):

    projects = Project.objects.all()
   
    return render(request, "projects/projects.html", {'projects': projects} )


def project(request, id):

    project = Project.objects.get(id=id)
    form = ProjectForm(instance = project)
    return render(request, "projects/project.html", {'project': project, 'form':form, 'request':request} )





