# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 03:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainers', '0005_remove_pokemon_stats_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='number',
            field=models.CharField(default='', max_length=10),
        ),
    ]