from rest_framework import serializers

from news.models import News


class NewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = News
        fields = "__all__"


class NewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = News
        fields = ("id", "title", "short_description", "img", "date_create")
