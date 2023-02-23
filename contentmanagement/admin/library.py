from django.contrib import admin

from contentmanagement.models import Library


@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'type')
