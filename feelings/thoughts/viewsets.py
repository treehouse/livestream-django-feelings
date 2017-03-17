from oauth2_provider.ext.rest_framework import IsAuthenticatedOrTokenHasScope
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from . import serializers
from .models import CONDITIONS

class ThoughtViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrTokenHasScope]
    serializer_class = serializers.ThoughtSerializer
    required_scopes = ['read', 'write']

    def get_queryset(self):
        return self.request.user.thoughts.all()


class ConditionsView(APIView):
    def get(self, request, format=None):
        conditions = [{'value': condition[0], 'label': condition[1], 'key': index}
                      for index, condition in enumerate(CONDITIONS)]
        return Response(conditions)

    def get_queryset(self):
        return self.request.user.thoughts.none()