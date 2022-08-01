from django.db.transaction import atomic
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers as srz
from rest_framework.exceptions import ValidationError

from . import models
from .models.quiz import Type


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


class QuizSerializer(srz.HyperlinkedModelSerializer):
    topics = TopicSerializer(many=True)
    questions = QuestionSerializer(many=True)

    class Meta:
        model = models.Quiz
        fields = [
            "url",
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
        extra_kwargs = {
            "user": {"read_only": True},
        }

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        instance = super(ResponseCreateSerializer, self).create(validated_data)
        return instance


class AnswerCreateSerializer(srz.ModelSerializer):
    class Meta:
        model = models.Answer
        fields = (
            "response",
            "question",
            "text",
            "options",
        )
        extra_kwargs = {
            "options": {
                "required": False,
                "allow_empty": True,
            },
        }

    def validate(self, attrs):
        response = attrs["response"]
        question = attrs["question"]
        text = attrs.get("text", "")
        options = attrs.get("options", [])

        if not response.quiz.questions.filter(id=question.id).exists():
            raise ValidationError(
                _("Quiz has not such a question"),
            )

        if question.type == Type.TEXT:
            if not text:
                raise ValidationError(
                    f"Text questions requires text answer",
                )
            if options:
                raise ValidationError(
                    "Text questions must not contain option answers",
                )

        if question.type == Type.SINGLE_CHOICE:
            if text:
                raise ValidationError(_("Answer must not contain text"))
            if len(options) != 1:
                raise ValidationError(_("Answer must contain exactly one option"))
            if options[0] not in question.options.all():
                raise ValidationError(_("Answer is not present in available options"))

        if question.type == Type.MULTIPLE:
            if text:
                raise ValidationError(_("Answer must not contain text"))
            for option in options:
                if option not in question.options.all():
                    raise ValidationError(
                        _("answer %s is not in options") % option.text
                    )

        if question.type == Type.MULTIPLE_WITH_OWN_ANSWER:
            for option in options:
                if option not in question.options.all():
                    raise ValidationError(_("Some answers are not available options"))

        return attrs

    @atomic
    def create(self, validated_data):
        response = validated_data["response"]
        question = validated_data["question"]

        validated_data["point"] = self.get_point(validated_data)
        response.total_point += validated_data["point"]
        if question.type in (
            Type.SINGLE_CHOICE,
            Type.MULTIPLE,
        ):
            validated_data["is_checked"] = True
        response.save()

        return super().create(validated_data)

    def get_point(self, validated_data):
        question = validated_data["question"]
        options = validated_data.get("options", [])
        result = 0

        if question.type == Type.SINGLE_CHOICE:
            if options[0].is_correct:
                result = question.max_point
        if question.type == Type.MULTIPLE:
            correct_options = question.options.filter(is_correct=True).count()
            point_per_correct_option = question.max_point / correct_options
            for option in options:
                if option.is_correct:
                    result += point_per_correct_option
                else:
                    result -= point_per_correct_option

        return result
