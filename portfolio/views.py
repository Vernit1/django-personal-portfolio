from django.shortcuts import render, redirect
from .models import Project, About
from .forms import ContactFormView
# from django.core.mail import send_mail

def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects})

def aboutme(request):
    return render(request, 'portfolio/aboutme.html')

def moreabout(request):
    projects = Project.objects.all()
    abouts = About.objects.all()
    return render(request, 'portfolio/moreabout.html', {'abouts':abouts, 'projects':projects})

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
            # send_mail(subject,content, contactemail, ["vernit.jain1@gmail.com"], fail_silently=False)
        except ValueError:
            return render(request, 'portfolio/contact.html', {'form':ContactFormView(), 'error':'Bad data passed in, Try again'})
    return render(request, 'portfolio/contact.html', {'success': 'Message Sent!'})
