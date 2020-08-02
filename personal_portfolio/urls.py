"""personal_portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from portfolio import views

urlpatterns = [
    path('dotesting/', admin.site.urls),
    path('', views.aboutme, name='aboutme'),
    path('about/', views.aboutme, name='aboutme'),
    path('moreabout/', views.moreabout, name='moreabout'),
    path('contactme/', views.contactme, name='contactme'),
    path('blog/', include('blog.urls')),
    path('todowoo/', include('todowoo.urls')),
    path('certificates/', include('certificates.urls')),
]
urlpatterns +=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
