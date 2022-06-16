from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from partner_site.models import ContactUs
from partner_site.serializers import ContactUsSerializer

# Create your views here.


class ContactUsCreate(ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
