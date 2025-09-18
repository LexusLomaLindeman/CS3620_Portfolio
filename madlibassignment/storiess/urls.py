from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('form/<int:id>/', views.form, name='form'),
     path('story/<slug:selectedStory>/', views.storySelected, name='storySelected'),

]