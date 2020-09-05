from django.contrib import admin
from .models import Note, ImageUploadInNote

class NoteAdmin(admin.ModelAdmin):
    list_display=('user', 'title', 'flag')
    list_per_page = 10
    search_fields =('title',)
    list_filter = ('user',)

    def flag_as_normal(self, request, queryset):
        count = queryset.update(flag='normal')
        self.message_user(request, '{} notes marked as normal.'.format(count))
    def flag_as_archieve(self, request, queryset):
        count = queryset.update(flag='archieve')
        self.message_user(request, '{} notes marked as archieve.'.format(count))
    actions=[flag_as_normal, flag_as_archieve]

class ImageUploadInNoteAdmin(admin.ModelAdmin):
    list_display=('user',)
    list_per_page = 10

admin.site.register(Note, NoteAdmin)
admin.site.register(ImageUploadInNote, ImageUploadInNoteAdmin)
