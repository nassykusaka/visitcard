# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-27 16:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_auto_20170127_0124'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='region',
            field=models.CharField(default='spb', max_length=32),
            preserve_default=False,
        ),
    ]