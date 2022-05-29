from rest_framework import serializers

from career.models import Career
from career.models import Country
from career.models import Direction


class CareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = "__all__"


class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = "__all__"


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"


class CareerListSerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)
    direction = DirectionSerializer(read_only=True)

    class Meta:
        model = Career
        fields = (
            "id",
            "name",
            "short_description",
            "remote",
            "office",
            "relocation",
            "direction",
            "country",
        )
