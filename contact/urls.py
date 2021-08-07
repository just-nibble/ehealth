from django.urls import path
from .models import Contact
from . import views

urlpatterns = [
    path("/", views.ContactListAPIView.as_view(), name="contact_list"),
    path("/<int:pk>/", views.ContactDetailAPIView.as_view(), name="contact_detail")
]
