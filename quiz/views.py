from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ViewSetMixin

from . import models
from . import serializers as srz
from .models import Response
from .serializers import RegistrationSerializer


class RegistrationView(generics.GenericAPIView):
    permission_classes = [AllowAny]

    serializer_class = RegistrationSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        name = user.get("name", "")
        email = user.get("email", "")
        username = user.get("username", "")
        password = user.get("password", "")

        users = get_user_model().objects.create(
            name=name,
            email=email,
            username=username,
            password=password,
        )
        users.set_password(password)
        users.save()

        return Response({"data": serializer.data, "status": status.HTTP_201_CREATED})


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
