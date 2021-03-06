from django.db import models
from django_countries.fields import CountryField

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    images = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)
    codeurl = models.URLField(blank=True)

    def __str__(self):
        return self.title

class About(models.Model):
    firstName = models.CharField(max_length=30, blank=True)
    lastName = models.CharField(max_length=30, blank=True)
    age = models.IntegerField(null=True, blank=True)
    country = CountryField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    mobile = models.IntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    languages = models.CharField(max_length=200,blank=True)
    yearOfExperience = models.IntegerField(null=True, blank=True)
    completedProject = models.IntegerField(null=True, blank=True)
    awardsWon = models.IntegerField(null=True, blank=True)
    users = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return "About - Vernit"

class ContactForm(models.Model):
    contactName = models.CharField(max_length=50)
    contactEmail = models.EmailField()
    subject = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return self.contactEmail

class Certificate(models.Model):
    name = models.CharField(max_length=200)
    issuedby = models.CharField(max_length=50)
    issuedDate = models.DateField()
    url = models.URLField(blank=True)
    file = models.FileField(blank= True, null=True,upload_to='certificates/')
    certificate = models.BooleanField(default=False)
    award = models.BooleanField(default=False)

    def __str__(self):
        return self.name
