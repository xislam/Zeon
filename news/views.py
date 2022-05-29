from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from news.models import News
from news.serializers import NewSerializer
from news.serializers import NewsSerializer


# Create your views here.


class NewsViewSet(viewsets.ViewSet):
    """
    A news ViewSet for listing or retrieving users.
    """

    def list(self, request):
        queryset = News.objects.all()
        serializer = NewsSerializer(queryset.order_by("-id"), many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = News.objects.all()
        news = get_object_or_404(queryset, pk=pk)
        serializer = NewSerializer(news)
        return Response(serializer.data)


class NewNews(viewsets.ViewSet):
    """New news 3 pieces"""

    def list(self, request):
        queryset = News.objects.all().order_by("-id")[:3]
        serializer = NewsSerializer(queryset, many=True)
        return Response(serializer.data)
