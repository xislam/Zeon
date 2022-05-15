from django.shortcuts import get_object_or_404
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from news.models import News
from news.serializers import NewsSerializer

# Create your views here.


class NewsViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """

    def list(self, request):
        queryset = News.objects.all()
        serializer = NewsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = News.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = NewsSerializer(user)
        return Response(serializer.data)
