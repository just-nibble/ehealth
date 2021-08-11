from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import ContactSerializer
from .models import Contact
from rest_framework import permissions
# Create your views here.


class ContactListAPIView(ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactDetailAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
