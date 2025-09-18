from django import forms
from .models import ContactInfo,Project

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactInfo
        fields = ['firstName', 'lastName', 'email', 'message']
        
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'image'] 