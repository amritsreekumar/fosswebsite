# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-20 18:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JoinApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('batch', models.CharField(choices=[('1st year', '1st year'), ('2nd year', 'wnd year'), ('3rd year', '3rd year'), ('4th year', '4t year')], max_length=100)),
                ('motivation', models.TextField()),
                ('cs_background', models.TextField(blank=True)),
                ('previous_work', models.TextField(blank=True)),
                ('interests', models.TextField()),
                ('date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('date',),
            },
        ),
    ]