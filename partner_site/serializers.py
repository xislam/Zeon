from rest_framework import serializers

from partner_site.models import Answer
from partner_site.models import ContactUs
from partner_site.models import CV
from partner_site.models import Direction
from partner_site.models import SocialNetwork


class SocialNetworkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SocialNetwork
        fields = "__all__"


class ContactUsSerializer(serializers.HyperlinkedModelSerializer):
    social_network = SocialNetworkSerializer(read_only=True)

    class Meta:
        model = ContactUs
        fields = "__all__"


class DirectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Direction
        fields = "__all__"


class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"


class CVSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CV
        fields = "__all__"
