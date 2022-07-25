from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from career.filter import CareerFilter
from career.models import Career
from career.models import Country
from career.models import CV
from career.models import Direction
from career.seriakizers import CareerListSerializer
from career.seriakizers import CareerSerializer
from career.seriakizers import CountryListSerializer
from career.seriakizers import CvSerializer
from career.seriakizers import DirectionListSerializer


class CareerViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Career.objects.all()
        serializer = CareerListSerializer(queryset, many=True)
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
    filter_fields = [
        "name",
        "remote",
        "office",
        "relocation",
        "direction__name",
    ]
    filter_class = CareerFilter
    search_fields = [
        "name",
        "remote",
        "office",
        "relocation",
        "direction__name",
        "country__name",
    ]


# class CareerCvCreate(viewsets.ViewSet):
#     def create(self, request, format=None):
#         serializer = CvSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CareerCvCreate(ModelViewSet):
    queryset = CV.objects.all()
    serializer_class = CvSerializer

    def pre_save(self, obj):
        obj.cv_file = self.request.FILES.get("file")


class NewCareer(viewsets.ViewSet):
    """New Career 3 pieces"""

    def list(self, request):
        queryset = Career.objects.all().order_by("-id")[:3]
        serializer = CareerSerializer(queryset, many=True)
        return Response(serializer.data)


class DirectionListViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Direction.objects.all()
        serializer = DirectionListSerializer(queryset, many=True)
        return Response(serializer.data)


class CountryListViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Country.objects.all()
        serializer = CountryListSerializer(queryset, many=True)
        return Response(serializer.data)
