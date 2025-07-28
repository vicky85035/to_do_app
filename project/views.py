from django.shortcuts import render
from rest_framework import generics, filters
from rest_framework.response import Response
from project.models import Organization, Project, Task
from project.serializers import OrganizationSerializer, ProjectSerializer, TaskSerializer
from project.pagination import SetPagination
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

class ProjectRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.filter(id=self.kwargs['pk'])
    
class TaskListAPIView(generics.ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        project_id = self.request.query_params.get('project_id')
        queryset = Task.objects.all()
        # breakpoint()
        if project_id:
            return queryset.filter(project_id=project_id)
        return queryset 
