from django.shortcuts import render,HttpResponse, redirect
from django.views import View
from site_2_process_instrument.forms import ContactForm
from django.core.mail import EmailMultiAlternatives
from site_2_process_instrument.models import AboutUs, ContactModel
from .utils import Util
from django.contrib.sites.shortcuts import get_current_site

# Create your views here.
def home(request):
    return render(request,"home/index.html")

def about(request):
    
    return render(request,"site2_instrument/project/about.html", {"text": AboutUs.objects.all()})

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            # if ContactModel.objects.filter(email).exists():
            form.save()
            current_site = get_current_site(request).domain
            # relativeLink = reverse('email-verify')
            absurl = 'http://'+current_site
            email_body = 'Hi '+name + \
                ' Use the link below to verify your email \n' + absurl
            data = {'email_body': email_body, 'to_email': email,
                    'email_subject': 'Verify your email'}
            Util.send_email(data)
            return render(request,"site2_instrument/project/contact.html")
    return render(request,"site2_instrument/project/contact.html")



