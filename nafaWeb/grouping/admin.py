
from django.contrib import admin
from django.shortcuts import render, redirect
from .models import *
from django.core.mail import send_mail
from .forms import SendEmailForm
# Register your models here.


class MyUserAdmin(admin.ModelAdmin):
    models = Group
    fields = []
    actions = ['Send_Email']

    def Send_Email(self, request, queryset):
        email = []
        for u in queryset:
            for i in u.user.all():
                email.append(i.email)

        print(type(email))
        form = SendEmailForm(initial={'users': email})

        return render(request, 'grouping/send_email.html', {'form': form})


admin.site.register(Group, MyUserAdmin)
