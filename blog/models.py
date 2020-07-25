from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    images = models.ImageField(upload_to='blog/images/', null=True)

    def __str__(self):
        return self.title
