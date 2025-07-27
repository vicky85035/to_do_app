from rest_framework import serializers
from accounts.models import User
from rest_framework.validators import UniqueValidator

class BasicUserserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'name',
            'username',
            'date_joined',
            'email',
            'profile_picture'
        ]

class MinimalUserSignupSerializer(serializers.Serializer):
        name = serializers.CharField(write_only=True, required=True)
        username = serializers.CharField(required=False)
        email = serializers.EmailField(
            required=True,
            validators=[
                UniqueValidator(
                    queryset=User.objects.all(),
                    message="A user with that email already exists.",
                )
            ],
        )
        password = serializers.CharField(write_only=True, required=True)
