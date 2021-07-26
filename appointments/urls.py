from django.urls import path, include
from .views import AppointmentListAPIView, AppointmentDetailAPIView
urlpatterns = [
    path('', AppointmentListAPIView.as_view(), name="appointment_list"),
    path('<int:pk>/', AppointmentDetailAPIView.as_view(), name="appointment_detail"),
]
