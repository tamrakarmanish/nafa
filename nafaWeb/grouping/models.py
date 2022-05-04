from django.db import models
from accounts.models import *

# Create your models here.


class Group(models.Model):
    name = models.CharField(max_length=200)
    user = models.ManyToManyField(
        Profile, related_name="group_members", blank=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


