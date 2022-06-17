from django.urls import include
from django.urls import path
from rest_framework import routers

from partner_site import views

router = routers.DefaultRouter()
router.register(r"contact_us/", views.ContactUsCreate, basename="ContactUs")
router.register(
    r"social_network/list", views.SocialNetworkList, basename="SocialNetwork"
)
router.register(r"direction/list", views.DirectionList, basename="Direction")
router.register(r"question_cv/list", views.QuestionCVList, basename="QuestionCVList")
router.register(r"answer/list", views.AnswerList, basename="AnswerList")
router.register(r"cv/create", views.PartnerCVCreate, basename="PartnerCV")

app_name = "partner_site"

urlpatterns = [path("", include(router.urls))]
