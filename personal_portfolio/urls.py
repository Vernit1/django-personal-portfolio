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
    path('keepnote/', include('keepnote.urls')),
    path('todowoo/', include('todowoo.urls')),
    path('certificates/', include('certificates.urls')),
    path('accounts/', include('allauth.urls')),
]
urlpatterns +=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
