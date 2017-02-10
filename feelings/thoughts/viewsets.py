from rest_framework import viewsets

from . import serializers


class ThoughtViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ThoughtSerializer

    def get_queryset(self):
        return self.request.user.thoughts.all()

    # def create(self, request, *args, **kwargs):
    #     import pdb
    #     pdb.set_trace()
    #     return super().create(request, *args, **kwargs)

