# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-31 10:24
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0032_auto_20161031_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='name',
            field=models.CharField(max_length=256, validators=[django.core.validators.RegexValidator(code='invalid_file_name', inverse_match=False, message='please enter a valid file name.', regex='^[a-zA-Z0-9_\\-](?:\\.|[a-zA-Z0-9_\\-])*$')], verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='sourcefile',
            name='name',
            field=models.CharField(max_length=256, validators=[django.core.validators.RegexValidator(code='invalid_file_name', inverse_match=False, message='please enter a valid file name.', regex='^[a-zA-Z0-9_\\-](?:\\.|[a-zA-Z0-9_\\-])*$')], verbose_name='name'),
        ),
    ]
