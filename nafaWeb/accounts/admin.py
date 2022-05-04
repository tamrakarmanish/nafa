#admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


# Register your models here.
class UserAdminConfig(UserAdmin):
    search_fields = ('email',)
    ordering = ('-start_date',)
    list_display = ('email','is_superuser')
    fieldsets = (
        ('General',{'fields':('email','password','first_name','last_name','maiden_name','gender','date_of_birth','graduate_year')}),
        ('Address',{'fields':('street_address','address2','city','state','zip','country_name')}),
        ('Permissions',{'fields':('is_staff','is_superuser')}),
    )
    add_fieldsets = (
        (None,{
            'classes':('wide',),
            'fields':('email','password1','password2')
        }),
        ('Permissions',{'fields':('is_staff','is_superuser')}),
    )

admin.site.register(Profile,UserAdminConfig)
