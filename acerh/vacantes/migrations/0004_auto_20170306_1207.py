# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-06 17:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacantes', '0003_aplicado_entrevista'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacante',
            name='pregunta',
            field=models.TextField(),
        ),
    ]
