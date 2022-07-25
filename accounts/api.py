from knox.models import AuthToken
from rest_framework import generics
from rest_framework import permissions
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from accounts.email import send_otp_via_email
from accounts.models import User
from accounts.serializers import LoginSerializer
from accounts.serializers import RegisterSerializer
from accounts.serializers import UserSerializer
from accounts.serializers import VerifyEmailSerializer


class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data

        return Response(
            {
                "user": UserSerializer(user).data,
                "token": AuthToken.objects.create(user)[1],
            }
        )


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        print(user.email)
        # send_otp_via_email(user.email, user.otp)
        return Response(
            {
                "user": UserSerializer(user).data,
                "token": AuthToken.objects.create(user)[1],
            }
        )


class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        self.request.user


class VerifyOPT(generics.GenericAPIView):
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
