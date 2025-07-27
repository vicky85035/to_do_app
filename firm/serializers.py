from rest_framework import serializers
from firm.models import Organization, Project, Task, TaskStatus, Tag,  Comment, Attachment, Notification

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['id', 'name', 'description', 'created_at']

class ProjectSerializer(serializers.ModelSerializer):
    client = OrganizationSerializer(read_only=True)
    # user = serializers.CharField(source='created_projects')

    class Meta:
        model = Project
        fields = ['id', 'name', 'start_date', 'status', 'client', 'members']


class TaskSerializer(serializers.ModelSerializer):
    project = serializers.CharField(source='tasks__name')
    user = serializers.StringRelatedField(source='created_tasks__name')

    class Meta:
        model = Task
        fields = ['id', 'tags', 'projects', 'title', 'user', 'progress', 'assigness', ]