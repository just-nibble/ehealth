from django.urls import path
from .serializers import UserSerializer
from . import views

urlpatterns = [
    path("", views.UserListAPIView.as_view(), name="user_list"),
    path("<int:pk>/", views.UserDetailAPIView.as_view(), name="user_detail"),
]

