from django.urls import path
from accounts.views import LoginAPIView, SignupAPIView

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login-apiview'),
    path('signup/', SignupAPIView.as_view(), name='signup-apiview'),
]