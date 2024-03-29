# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-03 10:21
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(null=True)),
                ('app_uuid', models.UUIDField(default=uuid.uuid4)),
                ('created', models.DateTimeField(auto_now=True)),
                ('enable', models.BooleanField(default=True)),
            ],
        ),
    ]
