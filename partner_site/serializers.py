from rest_framework import serializers

from partner_site.models import Answer
from partner_site.models import ContactUs
from partner_site.models import Direction
from partner_site.models import PartnerCV
from partner_site.models import QuestionCV
from partner_site.models import SocialNetwork


class SocialNetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialNetwork
        fields = "__all__"


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = "__all__"


class DirectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = "__all__"


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"


class QuestionCVSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionCV
        fields = "__all__"


class PartnerCVSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PartnerCV
        fields = "__all__"
