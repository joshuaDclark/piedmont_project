from django.views.generic import ListView, CreateView
from .models import Person, Question
from django.urls import reverse

#---------------Questionaire Form-----------------------#

class QuestionList(ListView):
    model = Question
