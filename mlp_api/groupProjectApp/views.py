from rest_framework import viewsets
from rest_framework.response import Response
from groupProjectApp.models import Group
from groupProjectApp.serializers import GroupSerializer
from rest_framework.permissions import IsAuthenticated

from rest_framework.decorators import action


class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = Group.objects.all()
        return queryset

    def list(self, *args, **kwargs):
        queryset = Group.objects.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)