from django.urls import path, include
from . import views

app_name='keepnote'

urlpatterns = [
    path('', views.login, name='login'),
    path('home', views.home, name='home')
]
