# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-27 18:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_organization_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='ldate',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='education',
            name='sdate',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='work',
            name='ldate',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='work',
            name='sdate',
            field=models.DateField(null=True),
        ),
    ]