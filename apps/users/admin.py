from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('email', 'is_staff', 'is_active', 'date_joined', 'last_login',)
    list_filter = ('is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': (
            'last_name',
            'first_name',
            'middle_name',
        )}),
        (_('Permissions'), {
            'fields': ('groups', 'is_active', 'is_staff', 'is_superuser', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_superuser', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )

    def get_fieldsets(self, request, obj=None):
        if not request.user.is_superuser:
            if obj is not None:
                return (
                    (None, {'fields': ('email', 'password')}),
                    (_('Personal info'), {'fields': (
                        'last_name',
                        'first_name',
                        'middle_name',
                    )}),
                    (_('Permissions'), {
                        'fields': ('groups', 'is_active', 'is_staff', 'user_permissions'),
                    }),
                    (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
                )
            else:
                return (
                    (None, {
                        'classes': ('wide',),
                        'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
                     ),
                )
        else:
            return super().get_fieldsets(request, obj)


admin.site.register(User, CustomUserAdmin)
