# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-14 01:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20171014_0120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='repository',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.RenameField(
            model_name='repository',
            old_name='tags_c',
            new_name='tags'
        ),
    ]
