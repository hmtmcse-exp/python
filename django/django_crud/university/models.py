import uuid

from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    app_uuid = models.UUIDField(default=uuid.uuid4)
    created = models.DateTimeField(auto_now=True)
    enable = models.BooleanField(default=True)
