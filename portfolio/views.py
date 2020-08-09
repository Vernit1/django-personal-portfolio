from django.shortcuts import render, redirect
from .models import Project, About, Certificate
from .forms import ContactFormView
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.template.loader import get_template
import requests

def certificates():
    certificate = Certificate.objects.filter(certificate = True).order_by('-issuedDate')
    return certificate
    # URLForAPI = "https://vernitjain.pythonanywhere.com/certificates/"
    # certificate = ""
    # try:
    #     response = requests.get(url = URLForAPI, timeout=0.1)
    #     certificate = response.json()
    # except:
    #     return certificate
    # return certificate

def awards():
    award = Certificate.objects.filter(award = True).order_by('-issuedDate')
    return award

def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects})

def aboutme(request):
    return render(request, 'portfolio/aboutme.html')

def moreabout(request):
    projects = Project.objects.all()
    abouts = About.objects.all()
    certificate = certificates()
    award = awards()
    return render(request, 'portfolio/moreabout.html', {'abouts':abouts, 'projects':projects, 'certificate': certificate, 'award':award})

def contactme(request):
    if request.method=="GET":
        return render(request, 'portfolio/contact.html', {'form':ContactFormView()})
    else:
        try:
            contactname=request.POST['contactName'].strip()
            contactemail=request.POST['contactEmail'].strip()
            subject=request.POST['subject'].strip()
            content=request.POST['content'].strip()
            if contactname == "":
                return render(request, 'portfolio/contact.html', {'error':'Please enter your name'})
            if contactemail == "":
                return render(request, 'portfolio/contact.html', {'error':'Please enter your email address'})
            if subject == "":
                return render(request, 'portfolio/contact.html', {'error':'Please enter the subject for mailing'})
            if content == "":
                return render(request, 'portfolio/contact.html', {'error':'Please enter message'})
            form=ContactFormView(request.POST)
            form.save()
            sendMail(contactname, contactemail, content, subject)
        except ValueError:
            return render(request, 'portfolio/contact.html', {'form':ContactFormView(), 'error':'Bad data passed in, Try again'})
    return render(request, 'portfolio/contact.html', {'success': 'Message Sent!'})

def sendMail(contactname, contactemail, content, subject):
    template = get_template("portfolio/contact_template.txt")
    context = {
        'contactname': contactname,
        'contactemail': contactemail,
        'content': content,
    }
    content = template.render(context)
    email = EmailMessage(
                subject,
                content,
                "contactname" +'',
                ['vernit.jain1@gmail.com'],
                headers = {'Reply-To': contactemail })
    email.send()
