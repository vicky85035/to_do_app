from django.urls import path
from firm.views import OrganizationListCreateAPIView

urlpatterns = [
    path('organization/', OrganizationListCreateAPIView.as_view(), name='oragnization-list-create-apiview'),
]