# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-07-12 12:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0103_auto_20170710_1817'),
    ]

    operations = [
        migrations.AddField(
            model_name='solutionrun',
            name='task_id',
            field=models.CharField(max_length=128, null=True, verbose_name='task id'),
        ),
    ]