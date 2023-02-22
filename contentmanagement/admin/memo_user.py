from django.contrib import admin

from contentmanagement.forms import UserForm
from contentmanagement.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    form = UserForm
    list_display = ('username', 'first_name', 'last_name')
