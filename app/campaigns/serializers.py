from rest_framework import serializers

from campaigns.models import AnswerChoice, Question


class AnswerChoiceSerializer(serializers.StringRelatedField):
    class Meta:
        model = AnswerChoice
        fields = ["answer_value"]


class SurveySerializer(serializers.ModelSerializer):
    answer_choices = AnswerChoiceSerializer(many=True)

    class Meta:
        model = Question
        fields = [
            "question_id",
            "question",
            "answer_choices",
            "answer_template",
            "active",
            "additional_info",
            "language",
        ]
