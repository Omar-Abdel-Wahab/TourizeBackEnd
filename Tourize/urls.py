"""Tourize URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from iteninary import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('housings/', views.HousingList.as_view()),
    path('restaurants/', views.RestaurantList.as_view()),
    path('transports/', views.TransportList.as_view()),
    path('activities/', views.ActivityList.as_view()),
    path('paths/', views.PathList.as_view()),
    path('iteninaries/', views.IteninaryList.as_view()),
    path('', views.home)
]
