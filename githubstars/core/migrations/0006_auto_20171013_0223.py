# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-13 02:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0005_auto_20171011_0329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='repository',
            name='username',
        ),
        migrations.AddField(
            model_name='repository',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
