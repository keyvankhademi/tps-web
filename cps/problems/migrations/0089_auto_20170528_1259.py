# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-05-28 12:59
from __future__ import unicode_literals

from django.db import migrations


def unique_testcase_set(testcases):
    names = {}
    for testcase in testcases.all():
        while testcase.name in names:
            cnt = names[testcase.name]
            names[testcase.name] = cnt + 1

            testcase.name = "{}({})".format(testcase.name, cnt)
        testcase.save()
        names[testcase.name] = 1


def unique_testcases(apps, schema_editor):
    from problems.models import InputGenerator, ProblemRevision

    disabled_generators = []

    print("disabling generators...")
    total = InputGenerator.objects.count()

    for i, generator in enumerate(InputGenerator.objects.all()):

        if i == 0 or 100 * (i - 1) // total != 100 * i // total:
            print("{}%".format(100 * i // total))

        if generator.is_enabled:
            generator.disable()
            disabled_generators.append(generator)

    print("renaming duplicate testcases!")
    total = ProblemRevision.objects.count()

    for i, problemRevision in enumerate(ProblemRevision.objects.all()):
        if i == 0 or 100 * (i - 1) // total != 100 * i // total:
            print("{}%".format(100 * i // total))
        unique_testcase_set(problemRevision.testcase_set.all())

    print('enabling disabled generators...')
    total = len(disabled_generators)

    for i, generator in enumerate(disabled_generators):
        if i == 0 or 100*(i-1)//total != 100*i//total:
            print("{}%".format(100*i//total))
        try:
            generator.enable()
        except:
            pass


class Migration(migrations.Migration):
    dependencies = [
        ('problems', '0088_problemdata_description'),
    ]

    operations = [
        migrations.RunPython(unique_testcases),

        migrations.AlterUniqueTogether(
            name='testcase',
            unique_together=set([('problem', 'name')]),
        ),
    ]