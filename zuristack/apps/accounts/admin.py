from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
from . import forms


@admin.register(models.CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = forms.CustomUserCreationForm
    form = forms.CustomUserChangeForm
    ordering = ['email']
    list_display = ["email", "is_staff", "is_active", "is_superuser"]
    search_fields = ["email"]
    fieldsets = (
        (None, {
            "fields": (
                'email', 'password'
            ),
        }),
        ('Details', {
            "fields": (
                'first_name', 'last_name', 'slug',
            ),
        }),
        ('Permissions', {
            "fields": (
                'is_staff', 'is_active',
            ),
        }),
    )
# Register your models here.
