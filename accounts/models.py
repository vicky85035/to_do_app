from django.db import models
from django.contrib.auth.models import AbstractUser # Recommended for custom user model

# 1. User Model (Custom User Model is highly recommended for future flexibility)
# You would typically set AUTH_USER_MODEL = 'yourapp.User' in settings.py
class User(AbstractUser):
    # Add any additional fields specific to your user profile here
    # For example, profile picture, phone number, etc.
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    # Add related_name to avoid clashes if AbstractUser already defines 'groups' or 'user_permissions'
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="custom_user_set", # Custom related_name
        related_query_name="custom_user",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="custom_user_set", # Custom related_name
        related_query_name="custom_user",
    )

    def __str__(self):
        return self.username

    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'