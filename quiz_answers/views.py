from rest_framework.response import Response
from rest_framework.views import APIView

from quiz_answers.email import send_otp_via_email
from quiz_answers.models import User
from quiz_answers.serializer import UserSerializer
from quiz_answers.serializer import VerifyEmailSerializer


class RegisterAPI(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = UserSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                send_otp_via_email(serializer.data["у"])
                return Response(
                    {
                        "status": 200,
                        "massage": "regist" "eration successufully check email",
                        "date": serializer.data,
                    }
                )
            return Response(
                {
                    "status": 400,
                    "message": "something wont wrent wrong",
                    "data": serializer.errors,
                }
            )
        except Exception as e:
            print(e)


class VerifyOPT(APIView):
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
