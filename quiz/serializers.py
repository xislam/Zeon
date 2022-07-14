from rest_framework import serializers as srz
from rest_framework.exceptions import ValidationError

from . import models
from .models import User
from .models.quiz import Type


class RegistrationSerializer(srz.ModelSerializer):
    class Meta:
        model = User
        fields = ["email"]


class TopicSerializer(srz.ModelSerializer):
    class Meta:
        model = models.Topic
        fields = ["name"]


class OptionSerializer(srz.ModelSerializer):
    class Meta:
        model = models.Option
        fields = [
            "id",
            "text",
        ]


class QuestionSerializer(srz.ModelSerializer):
    options = OptionSerializer(many=True)

    class Meta:
        model = models.Question
        fields = [
            "id",
            "time",
            "title",
            "img",
            "type",
            "options",
        ]


class QuizSerializer(srz.ModelSerializer):
    topics = TopicSerializer(many=True)
    questions = QuestionSerializer(many=True)

    class Meta:
        model = models.Quiz
        fields = [
            "id",
            "title",
            "topics",
            "short_description",
            "questions",
        ]


class ResponseCreateSerializer(srz.ModelSerializer):
    class Meta:
        model = models.Response
        fields = ("id", "quiz", "user")


class AnswerCreateSerializer(srz.ModelSerializer):
    class Meta:
        model = models.Answer
        fields = ("id", "response", "question", "text", "options")
        extra_kwargs = {
            "options": {"required": False},
        }

    def validate(self, attrs):
        question = attrs["question"]
        if question.type == Type.TEXT:
            if "text" not in attrs:
                raise ValidationError(
                    f"Text questions requires text answer",
                )
            if "options" in attrs:
                raise ValidationError(
                    "Text questions must not contain option answers",
                )
        if question.type == Type.SELECT:
            if "text" in attrs:
                raise ValidationError("Select question must not contain text answer")
            if "options" not in attrs:
                raise ValidationError("Select question must contain exactly one option")
            if attrs["options"]:
                pass
        return attrs

    def create(self, validated_data):
        super().create(validated_data)
