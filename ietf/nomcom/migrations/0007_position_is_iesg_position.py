# Copyright The IETF Trust 2020, All Rights Reserved
# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-01-07 14:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nomcom', '0006_auto_20190716_1216'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='is_iesg_position',
            field=models.BooleanField(default=False, verbose_name='Is IESG Position'),
        ),
    ]
