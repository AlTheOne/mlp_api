from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from userApp.models import (
    User,
    UserPersonalData,
    UserProgress,
    AccountActivationCode
)
from userApp.forms import UserCreationForm, UserChangeForm


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('login', 'email', 'phone', 'is_staff')
    list_display_links = ('login',)
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    seach_fields = ('login',  'email')
    ordering = ('login',)
    readonly_fields = ('date_of_creation', 'date_of_update')
    fieldsets = (
        (None, {'fields': ('login', 'password')}),
        ('Personal info', {'fields': ('phone', 'email', 'email_confirmed')}),
        ('Permissons', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
            )
        }),
        ('Important dates', {'fields': ('date_of_creation', 'date_of_update')})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'login', 'email', 'phone',
                'password1', 'password2'
            )
        }),
    )

@admin.register(UserPersonalData)
class UserProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(UserProgress)
class UserProgressAdmin(admin.ModelAdmin):
    pass

@admin.register(AccountActivationCode)
class AccountActivationAdmin(admin.ModelAdmin):
    list_display = ('code', 'user')
    list_display_links = ('code',)
    readonly_fields = ('code',)
    fields = ('code', 'user')
