from django import forms
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
# registration form

class RegistrationForm(UserCreationForm):

    # extend from the User class
    class Meta:
        model = Profile

        # define fields for the form
        
        fields = ['email','password1','password2','first_name','last_name','maiden_name','gender','date_of_birth','graduate_year','street_address','address2','city','state','zip','country_name']
        exclude=['is_active','is_staff','objects','user_permissions','groups','is_superuser','password','last_login']
        
        
class ProfileForm(forms.ModelForm):
    
    # extend from the User class
    class Meta:
        model = Profile

        # define fields for the form
        
        fields = ['email','first_name','last_name','maiden_name','gender','date_of_birth','graduate_year','street_address','address2','city','state','zip','country_name']
        exclude=['is_active','is_staff','objects','user_permissions','groups','is_superuser','password','last_login']