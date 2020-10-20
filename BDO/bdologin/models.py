from django.db import models
from django.utils import timezone
# Create your models here.

class Lead(models.Model):
    leadId = models.CharField(max_length=100)
    leadName = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone1 = models.CharField(max_length=100)
    choice = (
        ('Open', 'Open'),
        ('Open-Attempted to Contact', 'Open-Attempted to Contact'),
        ('Open-In Contact', 'Open-In Contact'),
        ('Closed-Succesfully', 'Closed-Succesfully'),
        ('Closed-Not Relevant', 'Closed-Not Relevant')
    )
    status = models.CharField(max_length=30, choices=choice)
    picture = models.ImageField(upload_to='images')
    company = models.CharField(max_length=200)
    contactPerson = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    leadRegisterDate = models.DateField(null=True)
    phone2 = models.CharField(max_length=100)
    websiteAddress = models.CharField(max_length=250)
    leadSource = models.CharField(max_length=200)
    leadIndustry = models.CharField(max_length=100)
    leadtype_choice = (
        ('Architecture Consultant', 'Architecture Consultant'),
        ('Client', 'Client')
    )
    leadType = models.CharField(max_length=30, choices=leadtype_choice)
    officeAddress = models.CharField(max_length=200)
    additionalNotes = models.CharField(max_length=200)

    def __str__(self):
        return self.leadName

class Followup(models.Model):
    lead_Id = models.CharField(max_length=100)
    lead_Name = models.CharField(max_length=100)
    date = models.DateField(null=True)
    contact_choice = (
        ('Phone', 'Phone'),
        ('E-mail', 'E-mail'),
        ('Direct Meeting', 'Direct Meeting')
    )
    contactSource = models.CharField(max_length=30, choices=contact_choice)
    description = models.CharField(max_length=200)
    notes = models.CharField(max_length=200)

