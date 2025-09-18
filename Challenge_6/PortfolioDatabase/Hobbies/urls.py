from django.urls import path, include
from . import views

urlpatterns =[
    path("", views.index, name="home"),
    path("hobbie/", views.hobbie, name="hobbie"),
    path("project/", views.project, name="project"),
    path("contact/", views.contact, name="contact"),
    path("details/<int:id>/<str:isHobbie>/", views.details, name="details"),
    path('thankyou/', views.thankyou, name="thankyou"),
    path('accounts/', include('django.contrib.auth.urls')),
    path("projectlist/", views.projectlist, name="projectlist"),
    path("projectform/", views.projectform, name="projectform"),
    path('project/delete/<int:id>/', views.deleteProject, name='deleteProject'),
]