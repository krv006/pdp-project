from django.contrib import admin
from django.contrib.admin import ModelAdmin

from users.forms import CustomAdminAuthenticationForm
from users.models import User

admin.AdminSite.login_form = CustomAdminAuthenticationForm


@admin.register(User)
class UserAdmin(ModelAdmin):
    list_display = 'username', 'first_name', 'last_name', 'email', 'is_active', 'type',
    list_editable = 'is_active', 'type',
    search_fields = 'email',
