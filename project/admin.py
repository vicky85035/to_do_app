from django.contrib import admin
from project.models import Organization, Project, Task, TaskStatus, Tag,  Comment, Attachment, Notification

# Register your models here.
admin.site.register([Organization, Project, Task, TaskStatus, Tag,  Comment, Attachment, Notification])