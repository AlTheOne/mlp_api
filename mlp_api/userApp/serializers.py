from rest_framework import serializers
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.password_validation import (
    validate_password,
    password_validators_help_texts as get_passw_helps
)
from userApp.models import User, AccountActivationCode

class UserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(
        label=_('password'),
        write_only=True,
        trim_whitespace=False,
        validators=[validate_password],
        help_text=_(' '.join(get_passw_helps()))
    )
    password2 = serializers.CharField(
        label=_('password confirmation'),
        write_only=True,
        trim_whitespace=False,
        help_text=_('Enter the same password as before.')
    )

    class Meta:
        model = User
        fields = ('login', 'email', 'phone', 'password1', 'password2')

    def validate_password2(self, password2):
        password1 = self.initial_data.get('password1')
        if password1 and password2 and password1 != password2:
            raise serializers.ValidationError("Passwords didn't match.")

        return password2

    def create(self, validated_data):
        user = User(
            login=validated_data['login'],
            email=validated_data['email'],
            phone=validated_data['phone']
        )
        user.set_password(validated_data['password2'])
        user.save()
        AccountActivationCode.objects.create(user=user)
        return user
