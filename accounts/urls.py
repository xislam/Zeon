from django.urls import path

from accounts.api import LoginAPI
from accounts.api import RegisterAPI
from accounts.api import UserAPI
from accounts.api import VerifyOPT


urlpatterns = [
    path("login/", LoginAPI.as_view()),
    path("register/", RegisterAPI.as_view()),
    path("user/", UserAPI.as_view()),
    path("users/email/verify/", VerifyOPT.as_view(), name="register"),
]
