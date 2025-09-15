from django.shortcuts import render
from .models import Hobbie, Project


# Create your views here.

def index(request):
    return render(request, 'hobbie/index.html')

def hobbie(request):
    hobbies = Hobbie.objects.all()
    context = {'hobbies':hobbies}
    return render(request, 'hobbie/hobbie.html',context)

def project(request):
    projects = Project.objects.all()
    context = {'projects':projects}
    return render(request, 'hobbie/project.html',context)

def contact(request):
    return render(request, 'hobbie/contact.html')

def details(request , id, isHobbie):
    isHobbie = isHobbie.lower() == "true"

    if isHobbie:
        cardSelected = Hobbie.objects.get(id=id)
    else:
       cardSelected = Project.objects.get(id=id)
     
    context = {
        "cardSelected": cardSelected,
        "isHobbie": isHobbie
    }

    return render(request, 'hobbie/details.html',context)