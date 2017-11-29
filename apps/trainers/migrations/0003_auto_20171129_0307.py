# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 03:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainers', '0002_auto_20171129_0104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemon',
            name='battle_sprite',
        ),
        migrations.RemoveField(
            model_name='pokemon',
            name='element_type',
        ),
        migrations.AddField(
            model_name='pokemon',
            name='ability_i',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='ability_ii',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='hidden_ability',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='number',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='stats_total',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='type_i',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='type_ii',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
