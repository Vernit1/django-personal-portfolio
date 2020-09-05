from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from datetime import datetime

def get_upload_path(instance, filename):
    return 'keepnote/{0}/{1}/{2}'.format(instance.user, instance.noteid, filename)

class MyStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        if self.exists(name):
            dir_name, file_name = os.path.split(name)
            file_root, file_ext = os.path.splitext(file_name)
            my_chars = '1'
            name = os.path.join(dir_name, '{}_{}{}'.format(file_root, my_chars, file_ext))
        return name

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=10000, null=True, blank=True)
    flag = models.CharField(max_length=20, default="normal")
    created = models.DateTimeField(default=datetime.now())

    def __str__(self):
        if self.title is None:
            return ""
        return self.title

class ImageUploadInNote(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    uploadFile = models.ImageField(blank= True, null=True,upload_to=get_upload_path, storage=MyStorage())
    noteid = models.IntegerField(null=True, blank=True)
