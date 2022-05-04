from .models import *
from .forms import *
from .filters import *

from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from django.core.mail import send_mail, BadHeaderError
from django import forms
from django.http import HttpResponse, HttpResponseRedirect


def event_details(request, id):
    event = Event.objects.get(id=id)
    context = {
        "event": event
    }
    return render(request, 'main/details/event-details.html', context)


def add_event(request):
    form = EventForm()
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            # print(request.POST['name'])
            form.save()
            return redirect("event:event_home")
    else:
        form = EventForm()
    return render(request, 'main/addAction/add-events.html', {"form": form, "label": "Add"})


def edit_event(request, id):
    event = Event.objects.get(id=id)
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect("event:event_home")

    else:
        form = EventForm(instance=event)
    return render(request, 'main/addAction/add-events.html', {"form": form, "label": "Edit"})


def event_home(request):
    events = Event.objects.all()
    context = {
        "events": events,
        "navbar": 'events'
    }
    return render(request, 'main/singleHome/event-home.html',  context)


def delete_event(request, id):
    event = Event.objects.get(id=id)
    event.delete()
    return redirect("event:event_home")


def userRegEvent(request, userId, eventId):
    if request.user.is_superuser or request.user.id == int(userId):
        event = Event.objects.get(id=eventId)
        user = Profile.objects.get(id=userId)
        event.user.add(user)
        return redirect("event:event_home")
    else:
        return redirect("main:home")


def getAllUsersInEvent(request, eventId):
    if request.user.is_superuser:
        event = Event.objects.get(id=eventId)
        users = event.user.all()
        myFilter = UserFilter(request.GET, queryset=users)
        users = myFilter.qs
        context = {
            "event": event,
            "users": users,
            'myFilter': myFilter
        }
        return render(request, 'main/eventActions/all_users_in_event.html', context)
    else:
        return redirect("main:home")


def getUserAllEvents(request, userId):
    if request.user.is_superuser or request.user.id == int(userId):
        user = Profile.objects.get(id=userId)
        events = Event.objects.filter(user=user)
        myFilter = EventFilter(request.GET, queryset=events)
        events = myFilter.qs

        context = {
            "events": events,
            "myFilter": myFilter,
            "user": user
        }
        return render(request, 'eventActions/all_events_of_user.html', context)
    else:
        return redirect("main:home")


def userLeaveEvent(request, eventId, userId):
    if request.user.is_superuser or request.user.id == int(userId):
        user = Profile.objects.get(id=userId)
        print(user)
        print(user.id)
        group = Event.objects.get(id=eventId)
        group.user.remove(user)
        return redirect('group:get_user_all_events', userId)
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
