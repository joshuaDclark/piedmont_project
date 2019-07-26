"""piedmontpuppies_project URL Configuration

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
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from piedmontpuppies_project.views import home_view, about_view, social_view
from registration.views import contact_detail_view, contact_create_view
from Questionaire.views import QuestionList
from account.views import AdminView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('social/', social_view, name='social'),
    path('contact/', contact_detail_view),
    path('create/', contact_create_view),
    path('questionaire/', QuestionList.as_view()),
    
 #accounts and login

    
    path('account/', include('account.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('', TemplateView.as_view(template_name='home.html'), name='Home'),
    path('administrator/', AdminView.as_view(template_name='admin/administrator.html'), name='administrator'),
]
