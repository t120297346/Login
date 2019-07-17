# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-07-17 07:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20190717_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='last_modify_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]