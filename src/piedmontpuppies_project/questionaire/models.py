import datetime
from django.db import models
from django.forms import ModelForm
from django.utils import timezone




class Person(models.Model):
    last_name = models.CharField(max_length=130, blank=False)
    first_name = models.CharField(max_length=130, blank=False)
    email = models.EmailField(blank=False)
    address = models.CharField(max_length=30, blank=False)
    city = models.CharField(max_length=30, blank=False)
    state = models.CharField(max_length=30, blank=False)
    zip_code = models.CharField(max_length=5, blank=False)
    phone = models.CharField(max_length=10, blank=False)
    date_created = models.DateField(auto_now_add=True)






class Question(models.Model):
    question_field = models.ForeignKey('Person', on_delete="CASCADE", 
    related_name="persons"
    )
    title = models.CharField(max_length=200)
    
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Choice(models.Model):
    question = models.ForeignKey('Question', on_delete="CASCADE",
    related_name="choices"
    )
    text = models.CharField(max_length=200)

    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text