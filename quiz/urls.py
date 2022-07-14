from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views
from .views import RegistrationView
from .views import VerifyOPT

app_name = "quiz"

router = DefaultRouter()
router.register("answer", views.AnswerViewSet, "answer")
router.register("quiz", views.QuizViewSet, "quiz")

router.register("response", views.ResponseViewSet, "response")

urlpatterns = [
    path("users/register/", RegistrationView.as_view(), name="register"),
    path("users/email/verify/", VerifyOPT.as_view(), name="register"),
]

urlpatterns += router.urls
