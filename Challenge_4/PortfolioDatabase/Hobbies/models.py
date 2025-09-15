from django.db import models

# Create your models here.
class Hobbie(models.Model):
    hobbie_name = models.CharField(max_length=64)
    hobbie_description = models.CharField(max_length=500)

    def __str__(self):
        return(f"ID: {self.id} Hobbie Name:{ self.hobbie_name} Hobbie Description: {self.hobbie_description}")

class Project(models.Model):
    project_name = models.CharField(max_length=64)
    project_description = models.CharField(max_length=500)
    
    def __str__(self):
        return(f"ID:{self.id} Project Name:{self.project_name} Project Description: {self.project_description}")
