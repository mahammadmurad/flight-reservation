"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from main import views
from main.routers import router as main_router
from flightApp.routers import router as flight_router
from flightApp import views
from rest_framework.authtoken.views import obtain_auth_token

# router = DefaultRouter()
# router.register('students', views.StudentViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(main_router.urls)),
    path("", include("main1.urls")),
    path("", include(flight_router.urls)),
    path("flightservice/", views.find_flights),
    path("flightservice/save-booking/", views.save_reservation),
    path('api-token-auth/', obtain_auth_token, name='apit-token-auth'),
]
