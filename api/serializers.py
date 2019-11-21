from rest_framework import serializers
from .models import Question

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = [
            'body'
        ]

        lookup_field = 'body'
        extra_kwargs = {
            'url': { 'lookup_field': 'body' }
        }