from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
import os

def get_upload_path(instance, filename):
    return 'todowoo/{0}/{1}/{2}'.format(instance.user, instance.todoid, filename)

class MyStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        if self.exists(name):
            dir_name, file_name = os.path.split(name)
            file_root, file_ext = os.path.splitext(file_name)

            my_chars = '1'  # The characters you want to append

            name = os.path.join(dir_name, '{}_{}{}'.format(file_root, my_chars, file_ext))
        return name

class Todo(models.Model):
    title= models.CharField(max_length=100)
    # uploadFile = models.FileField(blank= True, null=True,upload_to=get_upload_path, storage=MyStorage())
    memo = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted=models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    deleteTodoOrNot = models.BooleanField(default=False)

    def __str__(self):
        return "%s %s %s" % (self.user,"-",self.title)

class FileUpload(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    uploadFile = models.FileField(blank= True, null=True,upload_to=get_upload_path, storage=MyStorage())
    todoid = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.user)
