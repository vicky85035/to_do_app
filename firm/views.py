from django.shortcuts import render
from rest_framework import generics, filters
from firm.models import Organization, Project, Task
from firm.serializers import OrganizationSerializer, ProjectSerializer
from firm.pagination import SetPagination
# Create your views here.

class OrganizationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    pagination_class = SetPagination
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name', 'created_at']


class ProjectListCreateAPIView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = SetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'created_by__name']
    ordering_fields = ['created_at']

        # def get(self, request, *args, **kwargs):
        #     project_id = request.query_params.get('pk')
        #     return Task.objects.filter(project__id=project_id)