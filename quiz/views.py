from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.mixins import ListModelMixin
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSetMixin

from . import models
from . import serializers as srz


class QuizViewSet(
    ViewSetMixin,
    ListModelMixin,
    RetrieveModelMixin,
    GenericAPIView,
):
    serializer_class = srz.QuizSerializer
    queryset = models.Quiz.objects.all()


class ResponseViewSet(
    ViewSetMixin,
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    GenericAPIView,
):
    permission_classes = IsAuthenticated,

    def get_queryset(self):
        return models.Response.objects.filter(user=self.request.user)

    srz_map = {
        'create': srz.ResponseCreateSerializer,
    }

    def get_serializer_class(self):
        return self.srz_map.get(self.action, srz.ResponseCreateSerializer)


class AnswerViewSet(
    ViewSetMixin,
    CreateModelMixin,
    ListModelMixin,
    GenericAPIView,
):
    queryset = models.Answer.objects.all()

    srz_map = {
        'create': srz.AnswerCreateSerializer,
    }

    def get_serializer_class(self):
        return self.srz_map.get(self.action, srz.AnswerCreateSerializer)

    def create(self, request, *args, **kwargs):
        super(AnswerViewSet, self).create(request, *args, **kwargs)
        return Response(status=status.HTTP_201_CREATED)
