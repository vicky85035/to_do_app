from rest_framework import serializers
from firm.models import Organization, Project, Task, TaskStatus, Tag,  Comment, Attachment, Notification

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'