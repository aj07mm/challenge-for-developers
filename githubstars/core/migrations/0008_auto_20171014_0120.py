# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-14 01:20
from __future__ import unicode_literals

from django.db import migrations, models


def migrate_tags_model_to_string(apps, schema_editor):
    repository = apps.get_model('core', 'Repository')

    for repository in repository.objects.all():
        repository.tags_c = ', '.join(tag.name for tag in repository.tags.all())
        repository.save()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20171013_0317'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='repository',
            options={'ordering': ['name'], 'verbose_name': 'Repositório', 'verbose_name_plural': 'Repositórios'},
        ),
        migrations.AddField(
            model_name='repository',
            name='tags_c',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Tags'),
        ),
        migrations.RunPython(migrate_tags_model_to_string)
    ]