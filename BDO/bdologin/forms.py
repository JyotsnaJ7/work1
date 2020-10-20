from django.forms import ModelForm
from bdologin.models import Lead,Followup
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LeadCreateFrm(ModelForm):
    class Meta:
        model=Lead
        fields = '__all__'
        widgets = {
            'leadId': forms.TextInput(attrs={'class': 'form-control'}),
            'leadName': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'phone1': forms.TextInput(attrs={'class': 'form-control'}),
            'company': forms.TextInput(attrs={'class': 'form-control'}),
            'contactPerson': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'phone2': forms.TextInput(attrs={'class': 'form-control'}),
            'websiteAddress': forms.TextInput(attrs={'class': 'form-control'}),
            'leadSource': forms.TextInput(attrs={'class': 'form-control'}),
            'leadIndustry': forms.TextInput(attrs={'class': 'form-control'}),
            'officeAddress': forms.TextInput(attrs={'class': 'form-control'}),
            'additionalNotes': forms.TextInput(attrs={'class': 'form-control'}),
        }

class RegistrationFrm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','username','last_name','email','password1','password2']


class FollowupFrm(ModelForm):
    class Meta:
        model=Followup
        fields = '__all__'