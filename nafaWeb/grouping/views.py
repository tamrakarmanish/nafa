from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import *
from .forms import *
from .filters import *
from django.core.mail import send_mail, BadHeaderError
from django import forms
from django.http import HttpResponse, HttpResponseRedirect


# create group
def createGroup(request):
    if request.user.is_superuser:
        groupForm = GroupForm()
        if request.method == 'POST':
            groupForm = GroupForm(request.POST)
            if groupForm.is_valid():
                groupForm.save()

            return redirect("group:all_groups")

        context = {
            "groupForm": groupForm,
            "label": "Create"
        }

        return render(request, 'grouping/addGroup.html', context)
    else:
        return redirect("main:home")

# get all groups


def getAllGroups(request):
    myGroups = []
    if request.user.is_authenticated:
        grps= Group.objects.all()
        for group in grps:
            if request.user in group.user.all():
                myGroups.append(group)
                
    groups=Group.objects.all()
    myFilter = GroupFilter(request.GET,queryset=groups)
    groups = myFilter.qs

    context={
        "groups":groups,
        "myFilter":myFilter,
        "myGroups": myGroups
        }

# update group


def updateGroup(request, groupId):
    if request.user.is_superuser:
        group = Group.objects.get(id=groupId)
        groupForm = GroupForm(instance=group)
        if request.method == 'POST':
            groupForm = GroupForm(request.POST, instance=group)
            if groupForm.is_valid():
                groupForm.save()

            return redirect("group:all_groups")

        context = {
            "groupForm": groupForm,
            "label": "Update"
        }

        return render(request, 'grouping/addGroup.html', context)
    else:
        return redirect("main:home")


# delete group
def deleteGroup(request, groupId):
    if request.user.is_superuser:
        group = Group.objects.get(id=groupId)
        group.delete()

        return redirect("group:all_groups")
    else:
        return redirect("main:home")

# add user to a group


def userAddGroup(request, userId, groupId):
    if request.user.is_superuser or request.user.id == int(userId):
        group = Group.objects.get(id=groupId)
        print(group.name)
        user = Profile.objects.get(id=userId)
        group.user.add(user)
        return redirect("group:all_groups")
    else:
        return redirect("main:home")


# get all the users in a group
def getAllUsersInGroup(request, groupId):
    if request.user.is_superuser:
        group = Group.objects.get(id=groupId)
        users = group.user.all()
        myFilter = UserFilter(request.GET, queryset=users)
        users = myFilter.qs
        context = {
            "group": group,
            "users": users,
            'myFilter': myFilter
        }
        return render(request, 'grouping/all_users_in_group.html', context)
    else:
        return redirect("main:home")

# get all groups of a user


def getUserAllGroups(request, userId):
    if request.user.is_superuser or request.user.id == int(userId):
        user = Profile.objects.get(id=userId)
        groups = Group.objects.filter(user=user)
        myFilter = GroupFilter(request.GET, queryset=groups)
        groups = myFilter.qs

        context = {
            "groups": groups,
            "myFilter": myFilter,
            "user": user
        }
        return render(request, 'grouping/all_groups_of_user.html', context)
    else:
        return redirect("main:home")


def userLeaveGroup(request, groupId, userId):
    if request.user.is_superuser or request.user.id == int(userId):
        user = Profile.objects.get(id=userId)
        print(user)
        print(user.id)
        group = Group.objects.get(id=groupId)
        group.user.remove(user)
        return redirect('group:get_user_all_groups', userId)
    else:
        return redirect("main:home")


def email(request):
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')
    users = request.POST.get('users', '')
    users = users.replace("'", "")
    users = users.strip('][').split(', ')
    print(subject)
    print(message)
    print(users)

    if subject and message and users:
        try:
            send_mail(subject, message, 'sajinshrestha74@gmail.com',
                      users)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/admin')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')
