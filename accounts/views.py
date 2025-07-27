from django.shortcuts import render
from rest_framework import generics, status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from accounts.models import User
from accounts.serializers import BasicUserserializer, MinimalUserSignupSerializer
# Create your views here.

class LoginAPIView(generics.GenericAPIView):
    serializer_class = TokenObtainPairSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        # breakpoint()
        if not username or not password:
            return Response(
                {'detail': 'Both username or password are required.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            data = {}
            serializer = self.get_serializer(data=request.data)
            try:
                serializer.is_valid(raise_exception=True)
            except Exception as e:
                return Response(
                    {'detail': 'Invalid credentials.', "errors": serializer.errors},
                    status=status.HTTP_401_UNAUTHORIZED
                )
            
            data = {
                'user': BasicUserserializer(user).data,
                'token': serializer.validated_data,
            }

            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response (
                {'detail': 'Invalid credentails.'}, status=status.HTTP_401_UNAUTHORIZED,
            )
        
class SignupAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = MinimalUserSignupSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        name = serializer.validated_data['name']
        full_name = name.split()
        username = serializer.validated_data['username']
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        

        try:
            user = User(username=username, email=email, first_name=full_name[0], last_name=full_name[1])

            user.set_password(password)
            user.save()

            return Response(
                {
                    'message': 'User registered successfully!',
                    'username': user.username,
                    'email': user.email
                },
                status=status.HTTP_201_CREATED,
            )
        except Exception as e:
            return Response(
                {'detail': f'User registration failed: {str(e)}'},
                status=status.HTTP_400_BAD_REQUEST
            )