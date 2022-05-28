from django.urls import include
from django.urls import path
from rest_framework import routers

from news import views

router = routers.DefaultRouter()
router.register(r"news", views.NewsViewSet, basename="News")

app_name = "api_news"

urlpatterns = [path("", include(router.urls))]
