from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .Forms import ContactForm,ProjectForm
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
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save to database
            return redirect('/thankyou')
    else:
        form = ContactForm()
    return render(request, "hobbie/contact.html", {"form": form})

def thankyou(request):
    return render(request, "hobbie/thankyou.html")

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

@login_required
def projectlist(request):
    projects = Project.objects.all()
    context = {'projects':projects}
    return render(request, 'hobbie/projectlist.html',context)

def deleteProject(request, id):
    project = get_object_or_404(Project, id=id)
    project.delete()
    projects = Project.objects.all()
    context = {'projects':projects}
    return render(request, 'hobbie/projectlist.html',context)


def projectform(request):
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            projects = Project.objects.all()
            context = {'projects':projects}
            return render(request, 'hobbie/projectlist.html',context)
    else:
        form = ProjectForm()
    return render(request, "hobbie/projectform.html", {"form": form})
