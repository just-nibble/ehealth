from django.urls import path, include

urlpatterns = [
    path('register/', include('rest_auth.registration.urls')),
    path('', include('rest_auth.urls')),
    #path('rest-auth/registration/', include('rest_auth.registration.urls')),
]
