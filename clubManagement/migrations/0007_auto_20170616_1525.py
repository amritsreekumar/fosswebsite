# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-16 15:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clubManagement', '0006_auto_20170616_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
