from django.contrib import admin
from .models import Project, About, ContactForm, Certificate

myModels = [Project, About, ContactForm, Certificate]  # iterable list
admin.site.register(myModels)
