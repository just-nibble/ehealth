from django.urls import path
from . import views

urlpatterns = [
	path('', views.PlanListAPIView.as_view(), name="plan_list"),
	path('<int:pk>/', views.PlanDetailAPIView.as_view(), name="plan_detail"),
]