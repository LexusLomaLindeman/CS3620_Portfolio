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

class ContactInfo(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True)
    message = models.CharField(max_length=1000)
    
    def __str__(self):
        return(f"ID:{self.id} First Name:{self.firstName} Last Name:{self.lastName} Emial:{self.email} Message:{self.message}")

