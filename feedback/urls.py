from django.urls import include
from django.urls import path
from rest_framework import routers

from feedback import views

router = routers.DefaultRouter()
router.register(r"feedback/create", views.FeedbackCreate, basename="Feedback")

app_name = "feedback"

urlpatterns = [path("", include(router.urls))]
