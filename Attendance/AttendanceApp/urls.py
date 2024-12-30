"""
URL configuration for Attendance project.

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
# from django.contrib import admin
from django.urls import path
from AttendanceApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.signup_view, name='signup_view'),
    path('login_view', views.login_view, name='login_view'),
    path('logout_view', views.logout_view, name='logout_view'),
    path('data_view', views.data_view, name='data_view'),
    path('profile_view', views.profile_view, name='profile_view'),
    path('data_view', views.data_view, name='data_view'),
    path('superUser', views.superUser_view, name='superUser'),
]
# +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
