from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin

from users.forms import CustomAdminAuthenticationForm
from users.models import User

admin.AdminSite.login_form = CustomAdminAuthenticationForm


@admin.register(User)
class UserAdmin(ModelAdmin):
    pass
