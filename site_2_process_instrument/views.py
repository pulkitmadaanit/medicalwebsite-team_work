from django.shortcuts import render,HttpResponse, redirect
from django.views import View
from site_2_process_instrument.forms import ContactForm

from site_2_process_instrument.models import AboutUs, ContactModel

#imported by sunil
from .utils import Util
from django.contrib.sites.shortcuts import get_current_site

from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives




# Create your views here.
def home(request):
    return render(request,"home/index.html")

def about(request):
    
    return render(request,"site2_instrument/project/about.html", {"text": AboutUs.objects.all()})

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
           
            # if ContactModel.objects.filter(email).exists():
            form.save()
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            subject = "Scienco Medical "
    
            message = f'Hi {name}, your response has been submitted .'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail( subject, message, email_from, recipient_list )



    return render(request,"site2_instrument/project/contact.html")



