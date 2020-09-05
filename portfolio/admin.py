from django.contrib import admin
from .models import Project, About, ContactForm, Certificate

class ContactFormAdmin(admin.ModelAdmin):
    list_display=('contactName','contactEmail')
    list_per_page = 10

class ProjectAdmin(admin.ModelAdmin):
    list_display=('title', 'url', 'codeurl')
    list_per_page = 10
    list_editable=('url', 'codeurl')

class CertificateAdmin(admin.ModelAdmin):
    # readonly_fields = ('created',)
    list_display = ('name','issuedby','url','certificate', 'award')
    # list_editable=('title',)
    list_per_page = 10
    search_fields =('issuedby',)
    list_filter = ('certificate','award')
    list_display_links=('name',)
# myModels = [Project, About, ContactForm]  # iterable list
admin.site.register(Project, ProjectAdmin)
admin.site.register(About)
admin.site.register(ContactForm, ContactFormAdmin)
admin.site.register(Certificate, CertificateAdmin)
