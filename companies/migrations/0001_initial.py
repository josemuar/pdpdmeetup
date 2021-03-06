# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-25 14:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('abn', models.CharField(max_length=12)),
                ('description', models.CharField(max_length=200)),
                ('logo', models.ImageField(null=True, upload_to='images/')),
            ],
        ),
    ]
