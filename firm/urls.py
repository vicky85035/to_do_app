from django.urls import path
from firm.views import OrganizationListCreateAPIView, ProjectListCreateAPIView

urlpatterns = [
    path('organization/', OrganizationListCreateAPIView.as_view(), name='oragnization-list-create-apiview'),
    path('project/', ProjectListCreateAPIView.as_view(), name='project-list-create-apiview'),
]