# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-18 00:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0024_userp_pais_apli'),
    ]

    operations = [
        migrations.AddField(
            model_name='userp',
            name='telefono',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='userp',
            name='ar_exp',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='userp',
            name='ar_int',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='userp',
            name='carrera',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='userp',
            name='cat_licen',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='userp',
            name='cedula',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='userp',
            name='edad',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='userp',
            name='experiencia',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='userp',
            name='licencia',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='userp',
            name='localidad',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='userp',
            name='nacionalidad',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='userp',
            name='pais_apli',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='userp',
            name='sexo',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='userp',
            name='universidad',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
