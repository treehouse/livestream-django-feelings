from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from . import serializers
from .models import CONDITIONS

class ThoughtViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ThoughtSerializer

    def get_queryset(self):
        return self.request.user.thoughts.all()

    # def create(self, request, *args, **kwargs):
    #     import pdb
    #     pdb.set_trace()
    #     return super().create(request, *args, **kwargs)


class ConditionsView(APIView):
    def get(self, request, format=None):
        conditions = [{'value': condition[0], 'label': condition[1], 'key': index}
                      for index, condition in enumerate(CONDITIONS)]
        return Response(conditions)

    def get_queryset(self):
        return self.request.user.thoughts.none()