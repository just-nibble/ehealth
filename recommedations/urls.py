from django.urls import path
from .import views

urlpatterns = [
    path("", views.LocationRecommendationListAPIView.as_view(), name="recommendation_list"),
    path("doctor/", views.DoctorLocationRecommendationListAPIView.as_view(), name="doctor_recommendation"),
    path("hospital/", views.HospitalLocationRecommendationListAPIView.as_view(), name="hospital_recommendation"),
]
