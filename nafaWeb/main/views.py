from tokenize import group
from django.shortcuts import render, redirect

from .models import Scholarship, Campaign
from .forms import  MembershipForm, ScholarshipForm, CampaignForm
from HomePage.models import EditImage, EditAbout, EditOurTeam
from payments.models import Membership
from grouping.filters import *
from event.models  import *


# Create your views here.


def home(request):
    homeImageOne = EditImage.objects.get(id=1)
    homeImageTwo = EditImage.objects.get(id=2)
    homeImageThree = EditImage.objects.get(id=3)
    eventOne = Event.objects.get(id=8)
    eventTwo = Event.objects.get(id=6)
    scholarshipOne = Scholarship.objects.get(id=1)
    scholarshipTwo = Scholarship.objects.get(id=2)
    scholarshipThree = Scholarship.objects.get(id=3)
    editAbout = EditAbout.objects.get(id=1)
    editOurTeam = EditOurTeam.objects.all()

    context = {
        "homeImageOne": homeImageOne,
        "homeImageTwo": homeImageTwo,
        "homeImageThree": homeImageThree,
        "editAbout": editAbout,
        "scholarshipOne": scholarshipOne,
        "scholarshipTwo": scholarshipTwo,
        "scholarshipThree": scholarshipThree,
        "eventOne": eventOne,
        "eventTwo": eventTwo,
        "editOurTeam": editOurTeam,
        "navbar": 'home'
    }
   
    return render(request, 'main/index.html', context)




# def team_home(request):
#     teams = Team.objects.all()

#     context = {
#         "teams": teams,
#         "navbar": 'teams'
#     }
#     return render(request, 'main/singleHome/team-home.html', context)


def scholarship_home(request):
    scholarships = Scholarship.objects.all()

    context = {
        "scholarships": scholarships,
        "navbar": 'scholarships'
    }
    return render(request, 'main/singleHome/scholarship-home.html', context)


def campaign_home(request):
    campaigns = Campaign.objects.all()

    context = {
        "campaigns": campaigns,
        "navbar": 'campaigns'
    }
    return render(request, 'main/singleHome/campaign-home.html', context)


def membership_home(request):
    memberships = Membership.objects.all()
    context = {
        "memberships": memberships,
        "navbar": 'memberships'
    }
    return render(request, 'main/singleHome/membership-home.html', context)




def membership_details(request, id):
    membership = Membership.objects.get(id=id)
    context = {
        "membership": membership
    }
    return render(request, 'main/details/membership-details.html', context)



def add_membership(request):
    if request.method == "POST":
        form = MembershipForm(request.POST or None)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect("main:home")
    else:
        form = MembershipForm()
    return render(request, 'main/addAction/add-membership.html', {"form": form, "label": "Add"})



def edit_membership(request, id):
    membership = Membership.objects.get(id=id)
    if request.method == "POST":
        form = MembershipForm(request.POST, instance=membership)
        if form.is_valid():
            form.save()
            return redirect("main:home")

    else:
        form = MembershipForm(instance=membership)
    return render(request, 'main/addAction/add-membership.html', {"form": form, "label": "Edit"})




def delete_membership(request, id):
    membership = Membership.objects.get(id=id)
    membership.delete()
    return redirect("main:home")


# def team_details(request, id):
#     team = Team.objects.get(id=id)
#     context = {
#         "team": team
#     }
#     return render(request, 'main/details/team-details.html', context)


# def add_team(request):
#     if request.method == "POST":
#         form = TeamForm(request.POST or None)
#         if form.is_valid():
#             data = form.save(commit=False)
#             data.save()
#             return redirect("main:home")
#     else:
#         form = TeamForm()
#     return render(request, 'main/addAction/add-teams.html', {"form": form,
#                                                              "label": "Add"})


# def edit_team(request, id):
#     team = Team.objects.get(id=id)
#     if request.method == "POST":
#         form = TeamForm(request.POST, instance=team)
#         if form.is_valid():
#             form.save()
#             return redirect("main:home")

#     else:
#         form = TeamForm(instance=team)
#     return render(request, 'main/addAction/add-teams.html', {"form": form,
#                                                              "label": "Edit"})


# def delete_team(request, id):
#     team = Team.objects.get(id=id)
#     team.delete()
#     return redirect("main:home")
# def userRegEvent(request,userId,eventId):
#     if request.user.is_superuser or request.user.id == int(userId):
#         event = Event.objects.get(id=eventId)
#         print(event.name)
#         user = Profile.objects.get(id = userId)
#         event.user.add(user)
#         return redirect("main:user_reg_event")
#     else:
#         return redirect("main:home")



# def getAllUsersInEvent(request,eventId):
#     if request.user.is_superuser:
#         event = Event.objects.get(id = eventId)
#         users = event.user.all()
#         myFilter = UserFilter(request.GET,queryset=users)
#         users = myFilter.qs
#         context = {
#             "event":event,
#             "users":users,
#             'myFilter':myFilter
#         }
#         return render(request,'eventActions/all_users_in_event.html',context)
#     else:
#         return redirect("main:home")


# def getUserAllEvents(request,userId):
#     if request.user.is_superuser or request.user.id == int(userId):
#         user = Profile.objects.get(id = userId)
#         events = Event.objects.filter(user= user)
#         myFilter = EventFilter(request.GET,queryset=events)
#         events = myFilter.qs

#         context={
#             "events":events,
#             "myFilter":myFilter,
#             "user":user
#             }
#         return render(request,'eventActions/all_events_of_user.html',context)
#     else:
#         return redirect("main:home")


# def userLeaveEvent(request,eventId,userId):
#     if request.user.is_superuser or request.user.id == int(userId):
#         user = Profile.objects.get(id = userId)
#         print(user)
#         print(user.id)
#         group = Event.objects.get(id = eventId)
#         group.user.remove(user)
#         return redirect('group:get_user_all_events' ,userId)
#     else:
#         return redirect("main:home")


def scholarship_details(request, id):
    scholarship = Scholarship.objects.get(id=id)
    context = {
        "scholarship": scholarship
    }
    return render(request, 'main/details/scholarship-details.html', context)


def add_scholarship(request):
    if request.method == "POST":
        form = ScholarshipForm(request.POST or None)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect("main:home")
    else:
        form = ScholarshipForm()
    return render(request, 'main/addAction/add-Scholarships.html', {"form": form, "label": "Add"})


def edit_scholarship(request, id):
    scholarship = Scholarship.objects.get(id=id)
    if request.method == "POST":
        form = ScholarshipForm(request.POST, instance=scholarship)
        if form.is_valid():
            form.save()
            return redirect("main:home")

    else:
        form = ScholarshipForm(instance=scholarship)
    return render(request, 'main/addAction/add-scholarships.html', {"form": form, "label": "Edit"})


def delete_scholarship(request, id):
    scholarship = Scholarship.objects.get(id=id)
    scholarship.delete()
    return redirect("main:home")


def campaign_details(request, id):
    campaign = Campaign.objects.get(id=id)
    context = {
        "campaign": campaign
    }
    return render(request, 'main/details/campaign-details.html', context)


def add_campaign(request):
    if request.method == "POST":
        form = CampaignForm(request.POST or None)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect("main:home")
    else:
        form = CampaignForm()
    return render(request, 'main/addAction/add-Campaigns.html', {"form": form, "label": "Add"})


def edit_campaign(request, id):
    campaign = Campaign.objects.get(id=id)
    if request.method == "POST":
        form = CampaignForm(request.POST, instance=campaign)
        if form.is_valid():
            form.save()
            return redirect("main:home")

    else:
        form = ScholarshipForm(instance=campaign)
    return render(request, 'main/addAction/add-campaigns.html', {"form": form, "label": "Edit"})


def delete_campaign(request, id):
    campaign = Campaign.objects.get(id=id)
    campaign.delete()
    return redirect("main:home")
