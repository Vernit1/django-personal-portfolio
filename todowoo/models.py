from django.db import models
from django.contrib.auth.models import User

Status_choices=[('True', 'False')]

class Todo(models.Model):
    title= models.CharField(max_length=100)
    memo = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted=models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    deleteTodoOrNot = models.BooleanField(default=False, choices=Status_choices)

    def __str__(self):
        return "%s %s %s" % (self.user,"-",self.title)
