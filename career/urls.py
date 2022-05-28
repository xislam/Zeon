from django.urls import include
from django.urls import path
from rest_framework import routers

from career import views

router = routers.DefaultRouter()
router.register(r"career", views.CareerViewSet, basename="News")
router.register(r"career_filter", views.CareerListViewSet, basename="News")

app_name = "api_career"

urlpatterns = [path("", include(router.urls))]