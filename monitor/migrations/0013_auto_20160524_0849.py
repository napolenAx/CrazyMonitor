# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-24 08:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0012_auto_20160524_0807'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actioncondtion',
            name='severity',
        ),
        migrations.AlterUniqueTogether(
            name='actioncondtion',
            unique_together=set([('action', 'trigger')]),
        ),
    ]