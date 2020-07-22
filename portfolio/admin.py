from django.contrib import admin
from .models import Project, About, ContactForm

myModels = [Project, About, ContactForm]  # iterable list
admin.site.register(myModels)
