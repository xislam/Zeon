from rest_framework.routers import DefaultRouter

from . import views


app_name = "quiz"

router = DefaultRouter()
router.register("answer", views.AnswerViewSet, "answer")
router.register("quiz", views.QuizViewSet, "quiz")

router.register("response", views.ResponseViewSet, "response")

urlpatterns = []

urlpatterns += router.urls
