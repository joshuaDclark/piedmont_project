from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=50, null=True, blank=False)
    last_name = models.CharField(max_length=50, null=True, blank=False)
    phone_number = models.CharField(max_length=10, null=True, blank=False)
    email = models.EmailField(max_length=40, null=True, blank=False)
