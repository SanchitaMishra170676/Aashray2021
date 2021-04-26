from django.db import models
from django.utils import timezone

class Contact(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField(max_length=800)
    subject = models.CharField(max_length=300)
    email = models.EmailField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    answered =models.BooleanField(default=False)

    def __str__(self):
        return self.email 
    
class PlasmaDonorForm(models.Model):
    bloodGroup_choices = (
        ('A+','A+'),
        ('B+','B+'),
        ('AB+', 'AB+'),
        ('O+', 'O+'),
        ('A-', 'A-'),
        ('B-', 'B-'),
        ('AB-', 'AB-'),
        ('O-', 'O-')
    )
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=3)
    email = models.EmailField(max_length=255)
    contact = models.CharField(max_length=13,unique=True)
    bloodGroup = models.CharField(max_length=3, choices = bloodGroup_choices, default="A+")
    address = models.TextField(max_length=200)
    city = models.CharField(max_length=50)
    date = models.DateField()
    prevDonation = models.CharField(max_length=150)
    antibodies = models.CharField(max_length=150)
    medIssues = models.TextField(max_length = 500, blank= True)
    answered =models.BooleanField(default=False)
    verified = models.BooleanField(default=False)
    currDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email 
    
