"""examsproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from examapp import views
from django.conf.urls import url,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('python/', views.python_view),
    path('java/', views.java_view),
    path('aptitude/',views.aptitude_view),
    url(r'^home/', views.home_view),
    path('accounts/', include('django.contrib.auth.urls')),
    path('thanks/', views.thanks_view),
    path('first/', views.first_view),
    path('signup/', views.signup_view),
    path('firstquestion/',views.firstquestion),
    path('Secondquestion/',views.Secondquestion),
    path('Thirdquestion/',views.Thirdquestion),
    path('Fourthquestion/',views.Fourthquestion),
    path('Fifthquestion/',views.Fifthquestion),
    path('score/',views.Totalscore),


]
