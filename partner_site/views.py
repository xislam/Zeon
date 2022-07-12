from django.shortcuts import render
from rest_framework import generics
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from partner_site.models import ContactUs
from partner_site.models import Direction
from partner_site.models import PartnerAnswer
from partner_site.models import PartnerCV
from partner_site.models import QuestionCV
from partner_site.serializers import ContactUsSerializer
from partner_site.serializers import DirectionsSerializer
from partner_site.serializers import PartnerAnswerSerializer
from partner_site.serializers import PartnerCVSerializer
from partner_site.serializers import QuestionCVSerializer
from partner_site.serializers import SocialNetworkSerializer


class ContactUsCreate(mixins.CreateModelMixin, GenericViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer


class SocialNetworkList(mixins.ListModelMixin, GenericViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = SocialNetworkSerializer


class DirectionList(mixins.ListModelMixin, GenericViewSet):
    queryset = Direction.objects.all()
    serializer_class = DirectionsSerializer


class QuestionCVList(mixins.ListModelMixin, GenericViewSet):
    queryset = QuestionCV.objects.all()
    serializer_class = QuestionCVSerializer


class AnswerList(mixins.ListModelMixin, GenericViewSet):
    queryset = PartnerAnswer.objects.all()
    serializer_class = PartnerAnswerSerializer


class PartnerCVCreate(mixins.CreateModelMixin, GenericViewSet):
    queryset = PartnerCV.objects.all()
    serializer_class = PartnerCVSerializer

    def pre_save(self, obj):
        obj.cv_file = self.request.FILES.get("file")
