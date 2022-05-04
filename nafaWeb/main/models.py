import email
from email.mime import image
from pydoc import describe
from django.db import models
from django.utils import timezone

# from accounts.models import Profile

# class EventRsvp(models.Model):
#     event = models.ForeignKey(Event, related_name="event_members", on_delete=models.CASCADE, null=True, blank=True)
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.EmailField(max_length=50)
#     phone = models.IntegerField(max_length=11)
#     date = models.DateField(blank=True)
    
#     def __str__(self):
#         return self.event
    
#creating scholarship models here.
class Scholarship(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=2500)
    amount = models.DecimalField(max_digits = 50000, decimal_places= 2, default = 0.0)
    date = models.DateField()
    time = timezone.now()
    image = models.URLField(default = None, null= True, max_length=200)

    def __str__(self):
        return self.name

#creating campaing models here. 
class Campaign(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=2500)
    amount = models.DecimalField(max_digits = 50000, decimal_places= 2, default = 0.0)
    date = models.DateField()
    time = models.TimeField() 
    image = models.URLField(default = None, null= True, max_length=200)
    def __str__(self):
        return self.name
       
#creating campaing models here.
class Membership(models.Model):
    name= models.CharField(max_length=200 )
    description= models.TextField(max_length=500)
    image = models.URLField(default = None, null= True, max_length=200)
    amount = models.FloatField(null=True, blank=True)
    # validity: models.DateField()
    
    def __str__ (self):
        return self.name
    