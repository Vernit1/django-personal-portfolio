from django.forms import ModelForm
from .models import ContactForm

class ContactFormView(ModelForm):
    class Meta:
        model = ContactForm
        fields = ['contactName','contactEmail','subject','content']
