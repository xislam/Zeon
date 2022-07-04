from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

# QuizQuizfrom .views import QuizQuestion
# .ЙгшяЙгуыешщт№ акщь юмшуцы шьзщке КфтвщьЙгуыешщт

app_name = "quiz"

router = DefaultRouter()
router.register("answer", views.AnswerViewSet, "answer")
router.register("quiz", views.QuizViewSet, "quiz")
router.register("response", views.ResponseViewSet, "response")

urlpatterns = [
    # path("", Quiz.as_view(), name="quiz"),
    # path("r/<str:topic>/", RandomQuestion.as_view(), name="random"),
    # path("q/<str:topic>/", QuizQuestion.as_view(), name="questions"),
]

urlpatterns += router.urls
