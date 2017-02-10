from rest_framework import serializers

from . import models


class ThoughtSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Thought
        fields = ('recorded_at', 'condition', 'notes')

