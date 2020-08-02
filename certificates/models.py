from django.db import models

class Certificate(models.Model):
    name = models.CharField(max_length=200)
    issuedby = models.CharField(max_length=50)
    issuedDate = models.DateField()
    url = models.URLField(blank=True)
    file = models.FileField(blank= True, null=True,upload_to='certificates/')

    def __str__(self):
        return self.name
