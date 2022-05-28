from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.response import Response

from career.filter import CareerFilter
from career.models import Career
from career.seriakizers import CareerSerializer


class CareerViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Career.objects.all()
        serializer = CareerSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Career.objects.all()
        career = get_object_or_404(queryset, pk=pk)
        serializer = CareerSerializer(career)
        return Response(serializer.data)


class CareerListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Career.objects.all()
    serializer_class = CareerSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filter_fields = ["name", "shop_price"]
    filter_class = CareerFilter
    search_fields = [
        "name",
        "remote",
        "office",
        "relocation",
        "direction",
    ]
