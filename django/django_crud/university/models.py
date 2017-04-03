import uuid

from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    app_uuid = models.UUIDField(default=uuid.uuid4)
    created = models.DateTimeField(auto_now=True)
    enable = models.BooleanField(default=True)


class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    app_uuid = models.UUIDField(default=uuid.uuid4)
    created = models.DateTimeField(auto_now=True)
    enable = models.BooleanField(default=True)


class Student(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now=True)
    enable = models.BooleanField(default=True)
    app_uuid = models.UUIDField(default=uuid.uuid4)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course)


