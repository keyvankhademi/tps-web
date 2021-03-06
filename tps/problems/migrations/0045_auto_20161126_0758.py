# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-26 07:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0044_auto_20161125_2053'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solutionrun',
            name='is_valid',
        ),
        migrations.AlterField(
            model_name='solution',
            name='verdict',
            field=models.CharField(choices=[('correct', 'Correct'), ('time_limit', 'Time limit'), ('memory_limit', 'Memory limit'), ('incorrect', 'Incorrect'), ('runtime_error', 'Runtime error'), ('failed', 'Failed'), ('time_limit_and_runtime_error', 'Time limit / Runtime error')], max_length=50, verbose_name='verdict'),
        ),
    ]
