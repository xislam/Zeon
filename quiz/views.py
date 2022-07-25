from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import ViewSetMixin

from . import models
from . import serializers as srz


class QuizViewSet(
    ViewSetMixin,
    ListModelMixin,
    GenericAPIView,
):
    serializer_class = srz.QuizSerializer
    queryset = models.Quiz.objects.all()


class ResponseViewSet(
    ViewSetMixin,
    CreateModelMixin,
    ListModelMixin,
    GenericAPIView,
):
    queryset = models.Response.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return srz.ResponseCreateSerializer


class AnswerViewSet(
    ViewSetMixin,
    CreateModelMixin,
    ListModelMixin,
    GenericAPIView,
):
    queryset = models.Answer.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return srz.AnswerCreateSerializer
