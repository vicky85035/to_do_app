from django.urls import path
from firm.views import (
    OrganizationListCreateAPIView,
    ProjectListCreateAPIView,
    ProjectRetrieveUpdateDestroyAPIView,
    TaskListCreateAPIView,
)

urlpatterns = [
    path('organization/', OrganizationListCreateAPIView.as_view(), name='oragnization-list-create-apiview'),
    path('project/', ProjectListCreateAPIView.as_view(), name='project-list-create-apiview'),
    path('project/<int:pk>/', ProjectRetrieveUpdateDestroyAPIView.as_view(), name='project-retrieve-update-destroy-apiview'),
    path('task/', TaskListCreateAPIView.as_view(), name='task-list-create-apiview'),
]