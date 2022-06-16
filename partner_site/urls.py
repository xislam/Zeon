from django.urls import include
from django.urls import path
from rest_framework import routers

from partner_site import views

router = routers.DefaultRouter()
router.register(r"news", views.ContactUsCreate, basename="News")

app_name = "api_news"

urlpatterns = [path("", include(router.urls))]
