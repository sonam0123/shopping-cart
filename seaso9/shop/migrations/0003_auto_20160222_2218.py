# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-22 22:18
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20160222_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.FloatField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='pin',
            field=models.IntegerField(help_text=b'6 digit valid Postel code', validators=[django.core.validators.MaxValueValidator(999999), django.core.validators.MinValueValidator(100000)]),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[(b'initiated', b'Initiated'), (b'processing', b'Processing'), (b'dispatched', b'Dispatched')], default=b'initiated', max_length=20),
        ),
    ]
