from django.contrib.auth.forms import (
    UserCreationForm as BaseUserCreationForm,
    UserChangeForm as BaseUserChangeForm
)
from userApp.models import User


class UserCreationForm(BaseUserCreationForm):
    class Meta:
        model = User
        fields = ('login', 'email', 'phone')

class UserChangeForm(BaseUserChangeForm):
    class Meta:
        model = User
        fields = (
            'login', 'email', 'phone',
            'email_confirmed',
            'is_active', 'is_staff', 'is_superuser'
        )
