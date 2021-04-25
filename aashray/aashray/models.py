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
    