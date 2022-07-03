from django.urls import path

from quiz_answers.views import RegisterAPI
from quiz_answers.views import VerifyOPT

app_name = "quiz_answers"

urlpatterns = [
    path("register/", RegisterAPI.as_view(), name="register"),
    path("verify/email/", VerifyOPT.as_view()),
]
