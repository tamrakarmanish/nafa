from django.urls import path,re_path
from . import views 
from django.contrib.auth import views as auth_views

# set app name
app_name = "accounts"

urlpatterns = [
    path("login", views.login_user, name="login_user"),
    path("logout", views.logout_user, name="logout_user"),
    # re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     views.activate, name='activate'),
    path("activate/<uidb64>/<token>/", views.activate, name="activate"),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('register/', views.register_account, name="register_account"),
    path('profile/<uid>/', views.user_profile, name="user_profile"),
    path('editProfile/<uid>/', views.edit_profile, name="edit_profile")
]