from django.urls import include
from django.urls import path
from rest_framework import routers

from news import views

router = routers.DefaultRouter()
router.register(r"new", views.NewsModelViewSet, basename="New")
router.register(r"new_news", views.NewNews, basename="new_news")

app_name = "api_news"

urlpatterns = [path("", include(router.urls))]
