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
from django.urls import path
from piedmontpuppies_project.views import home_view, about_view, social_view
from registration.views import contact_detail_view, contact_create_view
from Questionaire.views import PersonCreateView


urlpatterns = [
    path('home/', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('social/', social_view, name='social'),
    path('contact/', contact_detail_view),
    path('create/', contact_create_view),
    path('questionaire/', PersonCreateView.as_view()),
    path('admin/', admin.site.urls),
]
