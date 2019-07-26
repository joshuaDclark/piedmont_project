from django.contrib import admin
from .models import Person, Question, Choice
admin.site.site_title = 'Administrator'
admin.site.site_header = 'Admin'

# Register your models here.


class PersonAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'date_created']
    list_filter = ['date_created']
    date_hierarchy = 'date_created'
    ordering = ['-date_created']





admin.site.register(Person, PersonAdmin)
admin.site.register(Question)
admin.site.register(Choice)