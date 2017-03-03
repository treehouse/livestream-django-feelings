from rest_framework import serializers

from . import models


class ThoughtSerializer(serializers.HyperlinkedModelSerializer):
    condition_display = serializers.SerializerMethodField()

    class Meta:
        model = models.Thought
        fields = ('id', 'recorded_at', 'condition', 'condition_display',
                  'notes', 'user')
        read_only_fields = ('id', 'recorded_at', 'user')

    def create(self, validated_data):
        thought = models.Thought(**validated_data)
        thought.user = self.context['request'].user
        thought.save()
        return thought

    def get_condition_display(self, obj):
        return obj.get_condition_display()
