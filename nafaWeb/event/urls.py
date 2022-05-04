from django.urls import path
from . import views

app_name = "event"

urlpatterns = [
    path("event-details/<int:id>/", views.event_details, name="event_details"),
    path("add-events/", views.add_event, name="add_event"),
    path("edit-event/<int:id>/", views.edit_event, name="edit_event"),
    path("delete-event/<int:id>", views.delete_event, name="delete_event"),
    path("event-home/", views.event_home, name="event_home"),
    path("<eventId>/user/<userId>/add",
         views.userRegEvent, name="user_reg_event"),
    path("<eventId>/all", views.getAllUsersInEvent,
         name="get_all_users_in_event"),
    path("all/user/<userId>", views.getUserAllEvents, name="get_user_all_events"),
    path("<eventId>/user/<userId>/leave",
         views.userLeaveEvent, name="user_leave_event"),
    path('', views.email, name='email')

]
