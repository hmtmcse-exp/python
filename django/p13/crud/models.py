from django.db import models


class Crud(models.Model):
    name = models.CharField(max_length=600)
    email = models.CharField(max_length=600)
    age = models.IntegerField()
