# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-27 20:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('file_repository', '0002_filemodel'),
        ('problems', '0003_auto_20160727_2022'),
    ]

    operations = [
        migrations.DeleteModel(
            name='File',
        ),
    ]
