import random

from _cffi_backend import string
from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ViewSetMixin

from . import models
from . import serializers as srz
from .email import send_otp_via_email
from .models import User
from .serializers import VerifyEmailSerializer


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


class RegistrationView(generics.GenericAPIView):
    permission_classes = [AllowAny]

    serializer_class = srz.RegistrationSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        otp = random.randint(10000000, 99999999)
        print(type(otp))
        email = user.get("email", "")
        users = get_user_model().objects.create(
            email=email,
            password=otp,
            otp=otp,
        )
        users.save()
        send_otp_via_email(email, otp)

        return Response({"data": serializer.data, "status": status.HTTP_201_CREATED})


class VerifyOPT(generics.GenericAPIView):
    permission_classes = [AllowAny]

    serializer_class = VerifyEmailSerializer

    def post(self, request):
        try:
            data = request.data
            serializer = VerifyEmailSerializer(data=data)

            if serializer.is_valid(raise_exception=True):
                email = serializer.data["email"]
                otp = serializer.data["otp"]
                user = User.objects.filter(email=email)
                if not user.exists():
                    return Response(
                        {
                            "status": 400,
                            "message": "something went wrong",
                            "data": "invaild email",
                        }
                    )
                if user[0].otp != otp:
                    return Response(
                        {
                            "status": 400,
                            "massage": "something went wrong",
                            "data": "wrong otp",
                        }
                    )
                user.first().is_verified = True
                user[0].save()

                return Response(
                    {
                        "status": 200,
                        "massage": "email verified",
                        "data": serializer.data,
                    }
                )
            return Response(
                {
                    "status": 400,
                    "massage": "something went wrong",
                    "data": serializer.data,
                }
            )

        except Exception as e:
            print(e)
