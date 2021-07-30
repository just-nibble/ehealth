from django.urls import path
from . import views

urlpatterns = [
    path("", views.FavouriteListAPIView.as_view(), name="favourite_list"),
    path("<int:pk>/", views.FavouriteDetailAPIView.as_view(), name="favourite_detail"),
]
