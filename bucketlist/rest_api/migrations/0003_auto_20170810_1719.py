# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-10 17:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('rest_api', '0002_auto_20170810_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='bucketlistdetail',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bucketlistdetail',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
