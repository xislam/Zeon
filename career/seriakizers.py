from rest_framework import serializers

from career.models import Career
from career.models import Country
from career.models import CV
from career.models import Direction


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


class CareerSerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)
    direction = DirectionSerializer(read_only=True)

    class Meta:
        model = Career
        fields = (
            "id",
            "name",
            "short_description",
            "description",
            "remote",
            "office",
            "relocation",
            "direction",
            "country",
        )


class CvSerializer(serializers.ModelSerializer):
    class Meta:
        model = CV
        fields = (
            "career",
            "name",
            "surname",
            "phone_number",
            "email",
            "cv_file",
        )


class DirectionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = ("name",)


class CountryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ("name",)
