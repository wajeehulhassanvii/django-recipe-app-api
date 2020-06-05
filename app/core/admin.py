from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# _ is for converting strings to human readable text,
# _ allows to pass through translation engine
from django.utils.translation import gettext as _

from core import models


class UserAdmin(BaseUserAdmin):
    # here we customize Admin
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        # if there is one field make it tuple by
        # adding one comma afterwards
        (_('Personal Info'), {'fields': ('name',)}),
        (
            _('Permissions'),
            {
                'fields': ('is_active', 'is_staff', 'is_superuser')
            }
        ),
        (_('Important dates'), {'fields': ('last_login',)})
    )
    add_fieldsets = (
        (None,
         {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
            },
         ),
    )


# it will register model.Users to UserAdmin
admin.site.register(models.User, UserAdmin)
