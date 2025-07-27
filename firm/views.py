from django.shortcuts import render
from rest_framework import generics
from firm.models import Organization
from firm.serializers import OrganizationSerializer
# Create your views here.

class OrganizationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer