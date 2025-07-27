from rest_framework import serializers
from firm.models import Organization, Project, Task, TaskStatus, Tag,  Comment, Attachment, Notification

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['id', 'name', 'description', 'created_at']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'