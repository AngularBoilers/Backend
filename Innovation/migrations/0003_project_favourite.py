# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-07-27 09:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Innovation', '0002_project_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='favourite',
            field=models.BooleanField(default=False),
        ),
    ]
