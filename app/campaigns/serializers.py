from rest_framework import serializers

from campaigns.models import Question


class SurveySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ["question_id", "question", "answer_choices", "answer_template", "active", "additional_info", "language"]