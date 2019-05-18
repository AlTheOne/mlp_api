from django.shortcuts import redirect
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    CreateModelMixin,
    RetrieveModelMixin,
    ListModelMixin
)
from rest_framework.response import Response
from userApp.models import User, AccountActivationCode
from userApp.serializers import UserSerializer


create_retrieve_list_interface = (
    CreateModelMixin, RetrieveModelMixin, ListModelMixin
)
class UserViewSet(*create_retrieve_list_interface, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'login'

class AccountActivationViewSet(GenericViewSet):
    serializer_class = UserSerializer
    lookup_field = 'code'

    def get_queryset(self):
        return AccountActivationCode.get_actuals()

    def retrieve(self, request, code=None):
        """
        Takes activation GET request (user has followed by activation link).
        Activates user account if activation code is correct.
        """
        code_obj = self.get_object()
        code_obj.user.email_confirmed = True
        code_obj.user.save()
        code_obj.delete()
        return redirect('/')

    def create(self, request):
        """
        Takes POST request for update activation link.
        """
        user = authenticate(
            login=request.data.get('login'),
            password=request.data.get('password')
        )

        if user is None:
            response_status = status.HTTP_401_UNAUTHORIZED
            response_text = "Authorization failed."
        elif user.email_confirmed:
            response_status = status.HTTP_400_BAD_REQUEST
            response_text = "Your account is already activated."
        else:
            if self.get_queryset().filter(user=user).exists():
                # Activation link already exists, so just send it to user:
                user.activation_code.notificate_user()
            else:
                # Remove expired link of the user:
                AccountActivationCode.objects.filter(user=user).delete()
                # Create new one:
                AccountActivationCode.objects.create(user=user)

            response_status = status.HTTP_200_OK
            response_text = "We have sent activation link on your email."

        return Response({'detail':response_text}, response_status)
