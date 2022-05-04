from django.urls import path
from . import views

app_name = "payments"

urlpatterns = [
    path("checkout/<int:id>/", views.checkout, name="checkout"),
    path("complete/", views.paymentComplete, name="complete")
]