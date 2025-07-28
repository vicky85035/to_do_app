from django.urls import path
from project.views import (
    OrganizationListCreateAPIView,
    ProjectListCreateAPIView,
    ProjectRetrieveUpdateDestroyAPIView,
    TaskListAPIView,
)

urlpatterns = [
    path('organization/', OrganizationListCreateAPIView.as_view(), name='oragnization-list-create-apiview'),
    path('<int:pk>/', ProjectRetrieveUpdateDestroyAPIView.as_view(), name='project-retrieve-update-destroy-apiview'),
    path('', ProjectListCreateAPIView.as_view(), name='project-list-create-apiview'),
    path('task/', TaskListAPIView.as_view(), name='task-list-apiview'),
]