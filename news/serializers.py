from rest_framework import serializers

from news.models import News


class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ("id", "title", "short_description", "img", "date_create")
