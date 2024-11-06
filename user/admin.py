from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from .models import User, Organization

# Custom admin for Organization model
@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']
    list_filter = ['created_at']


# Custom admin for User model
@admin.register(User)
class UserAdmin(DefaultUserAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email', 'is_org_admin', 'organization']
    search_fields = ['username', 'first_name', 'last_name', 'email']
    list_filter = ['is_org_admin', 'organization']
    
    
    autocomplete_fields = ['organization']

    
    # Customize fields displayed in the user form
    fieldsets = DefaultUserAdmin.fieldsets + (
        (None, {'fields': ('organization', 'is_org_admin')}),
    )

