# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-22 15:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('ip', models.GenericIPAddressField()),
                ('order', models.IntegerField()),
            ],
        ),
    ]
