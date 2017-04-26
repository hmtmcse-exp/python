import uuid

from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    app_uuid = models.UUIDField(default=uuid.uuid4)
    created = models.DateTimeField(auto_now=True)
    enable = models.BooleanField(default=True)

    @staticmethod
    def get_all_fields():
        return {
            'name': {
                'required': True,
                'message': 'Please Enter Name.'
            },
            'description': {},
            'enable': {},
        }


class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    app_uuid = models.UUIDField(default=uuid.uuid4)
    created = models.DateTimeField(auto_now=True)
    enable = models.BooleanField(default=True)

    @staticmethod
    def get_all_fields():
        return {
            'name': {
                'required': True,
                'message': 'Please Enter Name.'
            },
            'description': {},
            'enable': {},
        }


class Student(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200, null=True)
    created = models.DateTimeField(auto_now=True)
    enable = models.BooleanField(default=True)
    app_uuid = models.UUIDField(default=uuid.uuid4)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course)

    @staticmethod
    def get_all_fields():
        return {
            'first_name': {
                'required': True,
                'message': 'Please Enter First Name.'
            },
            'last_name': {},
            'enable': {},
            'department': {
                'required': True,
                'belongsTo': True,
                'modelName': "Department",
                'message': 'Please Select Department.'
            },
        }


