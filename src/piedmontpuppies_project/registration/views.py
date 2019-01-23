from django.shortcuts import render, HttpResponse
from .models import Contact
from .forms import ContactForm, RawContactForm
# Create your views here.

# def contact_create_view(request):
#     my_form = RawContactForm()
#     if request.method == "POST":
#         my_form = RawContactForm(request.POST)
#         if my_form.is_valid():
#             # now the data is good
#             print(my_form.cleaned_data)
#             Contact.objects.create(**my_form.cleaned_data)
#         else:
#             print(my_form.errors)
#
#     context = {
#         'form': my_form
#     }
#     return render(request, "registration/contact_create.html", context)



def contact_create_view(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ContactForm()

    context = {
        'form': form
    }
    return render(request, "registration/contact_create.html", context)




def contact_detail_view(request):
    obj = Contact.objects.get(id=1)
    context = {
        'object': obj
    }
    return render(request, "registration/contact_detail.html", context)


def questionaire_view(request):
    return render(request, "registration/questionaire.html")
