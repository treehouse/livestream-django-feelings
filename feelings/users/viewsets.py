from django.contrib.auth.models import User
from oauth2_provider.ext.rest_framework import IsAuthenticatedOrTokenHasScope

from rest_framework import viewsets

from . import serializers


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrTokenHasScope]
    queryset = User.objects.all()
    required_scopes = ['read', 'write']
    serializer_class = serializers.UserSerializer

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)
