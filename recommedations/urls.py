from django.urls import path
from .import views

urlpatterns = [
    path("", views.LocationRecommendationListAPIView.as_view(), name="recommendation_list")
]
