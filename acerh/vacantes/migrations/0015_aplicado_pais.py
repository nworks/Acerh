# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-06 21:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacantes', '0014_auto_20171106_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='aplicado',
            name='pais',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
