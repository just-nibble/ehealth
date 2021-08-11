from django.contrib import admin
from .models import CustomUser, Education, Experience
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.gis.admin import OSMGeoAdmin

# Register your models here.

@admin.register(CustomUser)
class UserAdmin(OSMGeoAdmin):

    fieldsets = (
        (None, {'fields': ('email', 'password', 'type', 'last_login', 'first_name', 'last_name', 'gender', 'phone', 'country', 'address', 'latitude', 'longitude', 'location')}),
        ('Permissions', {'fields': (
            'is_active', 
            'is_staff', 
            'is_superuser',
            'groups', 
            'user_permissions',
        )}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2')
            }
        ),
    )

    list_display = ('email', 'type', 'is_staff', 'last_login')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)

#admin.site.register(CustomUser, UserAdmin)
admin.site.register(Education)
admin.site.register(Experience)
