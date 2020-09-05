from django.contrib import admin
from .models import Todo, FileUpload

class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)
    list_display = ('user','title','datecompleted','deleteTodoOrNot', 'important')
    # list_editable=('title',)
    list_per_page = 10
    search_fields =('title',)
    list_filter = ('deleteTodoOrNot','important','datecompleted')
    list_display_links=('title',)

    def mark_as_delete(self, request, queryset):
        count = queryset.update(deleteTodoOrNot=True)
        self.message_user(request, '{} todo marked as deleted.'.format(count))

    def mark_as_not_delete(self, request, queryset):
        count = queryset.update(deleteTodoOrNot=False)
        self.message_user(request, '{} todo marked as not deleted.'.format(count))

    def created(self, obj):
        return obj

    actions=[mark_as_delete, mark_as_not_delete]

class FileUploadAdmin(admin.ModelAdmin):
    list_display = ('user','todoid')
    search_fields =('user',)

admin.site.register(Todo, TodoAdmin)
admin.site.register(FileUpload, FileUploadAdmin)
