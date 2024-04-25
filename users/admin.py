from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # Define fields to display in the user list
    list_display = ['username', 'email', 'is_admin', 'is_coach', 'is_agent', 'is_player']

    # Define fields for user detail view
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permissions', {'fields': ('is_admin', 'is_coach', 'is_agent', 'is_player')}),
    )

    # Add filter options
    list_filter = ['is_admin', 'is_coach', 'is_agent', 'is_player']
    search_fields = ['username', 'email']

    # Customize add and change forms
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_admin', 'is_coach', 'is_agent', 'is_player')}
        ),
    )

admin.site.register(CustomUser, CustomUserAdmin)
