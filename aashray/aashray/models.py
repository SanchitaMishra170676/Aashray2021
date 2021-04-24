from django.db import models
from django.utils import timezone

class Resource(models.Model):
    name = models.CharField(max_length=30)
    Image = models.ImageField(upload_to="media/Home/Resources/",default="")

    def __str__(self):
        return self.name 