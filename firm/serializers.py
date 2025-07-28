from rest_framework import serializers
from firm.models import Organization, Project, Task, TaskStatus, Tag,  Comment, Attachment, Notification
from accounts.models import User
from accounts.serializers import BasicUserserializer

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['id', 'name', 'description', 'created_at']

class ProjectSerializer(serializers.ModelSerializer):
    client = OrganizationSerializer(read_only=True)
    created_by = BasicUserserializer(read_only=True)
    # members = BasicUserserializer(read_only=True, many=True)  

    class Meta:
        model = Project
        fields = ['id', 'name', 'client', 'start_date', 'status', 'created_by', 'members']


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'tags', 'description', 'progress', 'assignees', ]