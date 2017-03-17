from oauth2_provider.ext.rest_framework import IsAuthenticatedOrTokenHasScope
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from . import serializers
from .models import CONDITIONS


class ThoughtPagination(LimitOffsetPagination):
    default_limit = 20
    max_limit = 20


class ThoughtViewSet(viewsets.ModelViewSet):
    pagination_class = ThoughtPagination
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