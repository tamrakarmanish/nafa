from operator import truediv
from django.utils import timezone
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager ,PermissionsMixin
from django.utils.translation import gettext_lazy as _
from main.models import *



# custom usermodel
class UserManager(BaseUserManager):
    use_in_migrations = True
    def create_user(self,email,password, **extra_fields):
        if not email:
            raise ValueError(_("Your must provide an email address"))
        
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True.')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True.')
        
        return self.create_user(email,password,**extra_fields)



class Profile(AbstractBaseUser, PermissionsMixin):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    maiden_name = models.CharField(max_length=200,blank=True,null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default="Select",blank=True,null=True)
    date_of_birth = models.DateField( blank=True, null=True)
    street_address = models.CharField(max_length=50,blank=True,null=True)
    address2 = models.CharField(max_length=10,blank=True,null=True)
    city = models.CharField(max_length=20,blank=True,null=True)
    state = models.CharField(max_length=20,blank=True,null=True)
    zip = models.CharField(max_length=5,blank=True,null=True)
    country_name = models.CharField(max_length=20,blank=True,null=True)
    graduate_year = models.CharField(max_length=4,blank=True,null=True)
    start_date = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff=models.BooleanField(_('is_staff'), default=False)
    objects = UserManager()
    # events = models.ManyToManyField(Event, related_name="member_event", blank=True, null=True)
    membership = models.ForeignKey(Membership, on_delete=models.CASCADE, blank=True, null=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']
