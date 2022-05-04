from django.db import models
from accounts.models import *

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=2500)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=500)
    image = models.URLField(default = None, null= True, max_length=200)
    user = models.ManyToManyField(Profile, related_name="members_in_event",blank=True)
    
    def __str__(self):
        return self.name