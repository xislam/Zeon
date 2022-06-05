from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Question
from .models import Quizzes
from .serializers import QuestionSerializer
from .serializers import QuizSerializer
from .serializers import RandomQuestionSerializer


class Quiz(generics.ListAPIView):
    serializer_class = QuizSerializer
    queryset = Quizzes.objects.all()


class RandomQuestion(APIView):
    def get(self, request, format=None, **kwargs):
        question = Question.objects.filter(quiz__title=kwargs["topic"]).order_by("?")[
            :1
        ]
        serializer = RandomQuestionSerializer(question, many=True)
        return Response(serializer.data)


class QuizQuestion(APIView):
    def get(self, request, format=None, **kwargs):
        quiz = Question.objects.filter(quiz__title=kwargs["topic"])
        serializer = QuestionSerializer(quiz, many=True)
        return Response(serializer.data)
