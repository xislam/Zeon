from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from feedback.serializers import FeedbackSerializer
from news.models import News
from news.serializers import NewSerializer
from news.serializers import NewsSerializer


# Create your views here.


class NewsModelViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewNews(viewsets.ViewSet):
    """New news 3 pieces"""

    def list(self, request):
        queryset = News.objects.all().order_by("-id")[:3]
        serializer = NewsSerializer(queryset, many=True)
        return Response(serializer.data)
