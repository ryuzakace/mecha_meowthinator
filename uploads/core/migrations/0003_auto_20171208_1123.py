# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-12-08 11:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20160801_0816'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='Phone',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AddField(
            model_name='document',
            name='YourName',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='document',
            name='location',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
