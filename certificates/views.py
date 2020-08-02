from django.shortcuts import render
from rest_framework import viewsets
from .models import Certificate
from .serializers import CertificateSerializer

class CertificateView(viewsets.ModelViewSet):
	queryset = Certificate.objects.all()
	serializer_class = CertificateSerializer
