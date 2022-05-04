from django.urls import path
from . import views


app_name = "main"

urlpatterns = [
    path("", views.home, name="home"),
    # path("event-details/<int:id>/", views.event_details, name="event_details"),
    # path("team-details/<int:id>/", views.team_details, name="team_details"),
    path("scholarship-details/<int:id>/",
         views.scholarship_details, name="scholarship_details"),
    path("campaign-details/<int:id>/",
         views.campaign_details, name="campaign_details"),
    path("membership-details/<int:id>/",
         views.membership_details, name="membership_details"),

    # path("add-events/", views.add_event, name="add_event"),
    # path("add-teams/", views.add_team, name="add_team"),
    path("add-scholarships/", views.add_scholarship, name="add_scholarship"),
    path("add-campaign/", views.add_campaign, name="add_campaign"),
    path("add-membership/", views.add_membership, name="add_membership"),

    # path("edit-event/<int:id>/", views.edit_event, name="edit_event"),
    # path("edit-team/<int:id>/", views.edit_team, name="edit_team"),
    path("edit-scholarship/<int:id>/",
         views.edit_scholarship, name="edit_scholarship"),
    path("edit-campaign/<int:id>/", views.edit_campaign, name="edit_campaign"),
    path("edit-membership/<int:id>/",
         views.edit_membership, name="edit_membership"),

    # path("delete-event/<int:id>", views.delete_event, name="delete_event"),
    # path("delete-team/<int:id>", views.delete_team, name="delete_team"),
    path("delete-scholarship/<int:id>",
         views.delete_scholarship, name="delete_scholarship"),
    path("delete-campaign/<int:id>", views.delete_campaign, name="delete_campaign"),
    path("delete-membership/<int:id>",
         views.delete_membership, name="delete_membership"),

    # path("event-home/", views.event_home, name="event_home"),
    # path("team-home/",  views.team_home, name="team_home"),
    path("scholarship-home/",  views.scholarship_home, name="scholarship_home"),
    path("campaign-home/", views.campaign_home, name="campaign_home"),
    path("membership-home/", views.membership_home, name="membership_home"),




    # path("<eventId>/user/<userId>/add", views.userRegEvent, name="user_reg_event"),
    # path("<eventId>/all", views.getAllUsersInEvent, name="get_all_users_in_event"),
    # path("all/user/<userId>", views.getUserAllEvents, name="get_user_all_events"),
    # path("<eventId>/user/<userId>/leave", views.userLeaveEvent, name="user_leave_event"),
]
