from django.contrib import admin
from .models import Project, About

myModels = [Project, About]  # iterable list
admin.site.register(myModels)
