from django.contrib import admin

from contentmanagement.forms import UserForm
from contentmanagement.models import User, Library, LibraryFile, Attachment


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    form = UserForm
    list_display = ('username', 'first_name', 'last_name')


@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'type')


@admin.register(LibraryFile)
class LibraryFileAdmin(admin.ModelAdmin):
    list_display = ('library', 'file_name', 'description')


@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    list_display = ('library_file', 'file_name', 'field')
