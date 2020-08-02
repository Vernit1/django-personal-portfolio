from django.contrib import admin
from .models import Todo, FileUpload

@admin.register(Todo, FileUpload)
class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

    def created(self, obj):
        return obj
