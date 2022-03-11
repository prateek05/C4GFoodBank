from rest_framework import serializers

from campaigns.models import Response, Question


class SurveySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ["question_id", "question", "answer_choices", "answer_template", "active", "additional_info", "language"]

class SurveyResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Response
        fields = ["question_id", "location", "value", "language"]
    
    def create(self, validated_data):
        return Response.objects.create(**validated_data)