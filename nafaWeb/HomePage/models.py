from pydoc import describe
from statistics import mode
from django.db import models

# class pastEvent(models.Model):
#     image = models.ImageField(blank=True, null=True, upload_to="newPicture/")
#     firstDescription= models.CharField(max_length=200)
#     secondDescription = models.CharField(max_length=200)
#     def __str__(self):
#         return self.firstDescription

# # Create your models here.
# class ImageSection(models.Model):
#     heading = models.CharField(max_length=200)
#     image = models.URLField(max_length=2000)
#     firstDescription= models.CharField(max_length = 200)
#     secondDescription= models.CharField(max_length = 200)

#     def __str__(self):
#         return self.heading

# # Create your About section here.
# class AboutHomePage(models.Model):
#     heading = models.CharField(max_length=200)
#     firstDescription= models.CharField(max_length=200)
#     secondDescription = models.CharField(max_length=200)
#     image = models.URLField(max_length=2000, default=None, null=True)
#     def __str__(self):
#         return self.heading

# # Create your Event section here
# class AboutPayments(models.Model):
#     heading = models.CharField(max_length=200)
#     firstDescription= models.CharField(max_length=200)
#     secondDescription = models.CharField(max_length=200)

#     def __str__(self):
#         return self.heading


# Create your About section here.
class EditImage(models.Model):
    heading = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    image = models.URLField(max_length=2000, default=None, null=True)

    def __str__(self):
        return self.heading


class EditAbout(models.Model):
    heading = models.CharField(max_length=50)
    sub_heading = models.CharField(max_length=50)
    sub_description = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.URLField(max_length=2000, default=None, null=True)

    def __str__(self):
        return self.heading


class EditOurTeam(models.Model):
    name = models.CharField(max_length=25)
    position = models.CharField(max_length=25)
    description = models.CharField(max_length=50)
    image = models.URLField(max_length=2000, default=None, null=True)

    def __str__(self):
        return self.name
