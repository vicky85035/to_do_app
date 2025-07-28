from django.shortcuts import render
from rest_framework import generics, status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from accounts.models import User
from accounts.serializers import BasicUserserializer, MinimalUserSignupSerializer
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.

class LoginAPIView(generics.GenericAPIView):
    serializer_class = TokenObtainPairSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        password = request.data.get("password")
        # breakpoint()
        if not email or not password:
            return Response(
                {'detail': 'Both email or password are required.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = authenticate(request, email=email, password=password)

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
            
            token = serializer.validated_data

            data = {
                'user': BasicUserserializer(user).data,
                'access': token['access'],
                'refresh': token['refresh'],
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
        username = serializer.validated_data.get('username')
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        name_parts = name.split()

        if len(name_parts) == 0:
            first_name = ""
            last_name = ""
        elif len(name_parts) == 1:
            first_name = name_parts[0]
            last_name = ""
        else:
            first_name = name_parts[0]
            last_name = name_parts[1]

        try:
            user = User(username=username, email=email, first_name=first_name, last_name=last_name)

            user.set_password(password)
            user.save()
            token = RefreshToken.for_user(user)
            # breakpoint()

            return Response(
                {
                    'user': BasicUserserializer(user).data,
                    'refresh': str(token),
                    'access': str(token.access_token)
                },
                status=status.HTTP_201_CREATED,
            )
        except Exception as e:
            return Response(
                {'detail': f'User registration failed: {str(e)}'},
                status=status.HTTP_400_BAD_REQUEST
            )