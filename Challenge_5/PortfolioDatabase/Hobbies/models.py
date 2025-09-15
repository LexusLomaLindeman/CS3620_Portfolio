from django.db import models

# Create your models here.
class Hobbie(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=500)
    image = models.ImageField(blank=False)

    def __str__(self):
        return(f"ID: {self.id} Hobbie Name:{ self.name} Hobbie Description: {self.description}")

class Project(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=500)
    image = models.ImageField(blank=False)
    
    def __str__(self):
        return(f"ID:{self.id} Project Name:{self.name} Project Description: {self.description}")
