from django.urls import path
from .models import Contact
from . import views

urlpatterns = [
    path("/", views.ContactListAPIView, name="contact_list"),
    path("/<int:pk>/", views.ContactDetailAPIView, name="contact_detail")
]
