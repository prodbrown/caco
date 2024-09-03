from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import CustomUser

class UserAdmin(BaseUserAdmin):
    # Fields to be used in displaying the User model in the admin
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'middle_name', 'surname', 'nida_number', 'phone_number_1', 'phone_number_2', 'passport_image')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login',)}),  # Removed 'date_joined'
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'surname', 'gender', 'phone_number_1', 'is_staff', 'is_superuser'),
        }),
    )
    
    list_display = ('email', 'first_name', 'surname', 'is_staff')
    search_fields = ('email', 'first_name', 'surname')
    ordering = ('email',)

# Register the custom user model with the UserAdmin class
admin.site.register(CustomUser, UserAdmin)
