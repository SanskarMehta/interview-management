from django.contrib import admin
from .models import CustomUser , user_details , interviewer_details
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            "User role",
            {
                'fields': (
                    'Is_interviewer',
                    'Is_first_time',
                )
            }
        )
    )

admin.site.register(interviewer_details)
admin.site.register(user_details)
admin.site.register(CustomUser, CustomUserAdmin)
