from django.urls import path
from . import views

urlpatterns =[
    path("", views.index, name="home"),
    path("hobbie/", views.hobbie, name="hobbie"),
    path("project/", views.project, name="project"),
    path("contact/", views.contact, name="contact"),
    path("details/<int:id>/<str:isHobbie>/", views.details, name="details"),
]