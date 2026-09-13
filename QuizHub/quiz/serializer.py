from rest_framework import serializers
from models import *

class OptionSerializer(serializers.ModelSerializer):
     class Meta:
        model = Option
        fields = [ "id", "question", "option_text", "is_correct", ]


class QuestionSerializer(serializers.Model):
    class Meta:
        model = Question
        fields = [
            "id",
            "quiz",
            "question_text",
            "options",
        ]

class QuizSerializer(serializers.ModelSerializer):

    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Quiz
        fields = [
            "id",
            "title",
            "description",
            "duration",
            "created_at",
            "questions",
        ]

class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = [
            "id",
            "name",
            "age",
            "gender",
            "institution",
            "class_name",
        ]