from rest_framework import serializers

from .models import Answer
from .models import Question
from .models import Quizzes
from .models import Topic


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ["name"]


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = [
            "id",
            "answer_text",
            "is_right",
        ]


class RandomQuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = "__all__"


class QuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = [
            "id",
            "time",
            "title",
            "img",
            "answer",
        ]


class QuizSerializer(serializers.ModelSerializer):
    topic = TopicSerializer(read_only=True, many=True)
    question = QuestionSerializer(read_only=True, many=True)

    class Meta:
        model = Quizzes
        fields = [
            "id",
            "title",
            "topic",
            "short_description",
            "question",
        ]
