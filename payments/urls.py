from django.urls import path
from . import views

urlpatterns = [
	path('', views.PlanListView.as_view(), name="plan_list")
]