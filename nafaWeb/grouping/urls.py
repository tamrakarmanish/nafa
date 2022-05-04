from django.urls import path
from . import views, admin
from django.contrib.auth import views as auth_views

# set app name
app_name = "grouping"

urlpatterns = [
    path("all", views.getAllGroups, name="all_groups"),
    path("create", views.createGroup, name="create_group"),
    path("update/<groupId>", views.updateGroup, name="update_group"),
    path("delete/<groupId>", views.deleteGroup, name="delete_group"),
    path("<groupId>/user/<userId>/add",
         views.userAddGroup, name="user_add_group"),
    path("<groupId>/all", views.getAllUsersInGroup,
         name="get_all_users_in_group"),
    path("all/user/<userId>", views.getUserAllGroups, name="get_user_all_groups"),
    path("<groupId>/user/<userId>/leave",
         views.userLeaveGroup, name="user_leave_group"),
    path('', views.email,
         name='email'
         )
]
