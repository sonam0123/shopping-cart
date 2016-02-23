# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-17 05:20
from __future__ import unicode_literals

from django.db import migrations, models
import inventory.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('price', models.FloatField()),
                ('image', models.ImageField(upload_to=inventory.models.image_upload_path)),
                ('description', models.TextField()),
                ('stock', models.IntegerField()),
            ],
        ),
    ]