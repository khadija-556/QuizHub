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

class QuizAttemptSerializer(serializers.ModelSerializer):
    answers = serializers.PrimaryKeyRelatedField(many=True,read_only=True)

    class Meta:
        model = QuizAttempt
        fields = [
            "id",
            "participant",
            "quiz",
            "score",
            "started_at",
            "completed_at",
            "answers",
        ]

        read_only_fields = [
            "score",
            "started_at",
            "completed_at",
        ]

class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = [
            "id",
            "attempt",
            "question",
            "selected_option",
            "is_correct",
        ]

        read_only_fields = [
            "is_correct",
        ]

    def validate(self,data):
        question = data["question"]
        selected_option = data["selected_option"]