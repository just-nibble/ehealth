from django.urls import path
from . import views

urlpatterns = [
    path("", views.CouponListAPIView.as_view(), name="coupon_list"),
    path("<int:pk>/", views.CouponDetailAPIView.as_view(), name="coupon_detail"),
]
