from rest_framework import serializers
from .models import Certificate

class CertificateSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Certificate
		fields = ('name', 'issuedby', 'issuedDate','url','file')
