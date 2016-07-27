# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-24 08:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('monitor', '0010_remove_action_conditions'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('phone', models.IntegerField(blank=True, max_length=15, null=True)),
                ('weixin', models.CharField(blank=True, max_length=64, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='actionoperation',
            name='msg_format',
            field=models.TextField(default=b'Host({hostname},{ip}) service({service_name}) has issue,msg:{msg}', verbose_name='\u6d88\u606f\u683c\u5f0f'),
        ),
        migrations.AddField(
            model_name='actionoperation',
            name='notifiers',
            field=models.ManyToManyField(blank=True, to='monitor.UserProfile', verbose_name='\u901a\u77e5\u5bf9\u8c61'),
        ),
    ]