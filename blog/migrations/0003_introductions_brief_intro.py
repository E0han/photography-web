# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 15:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20171130_1414'),
    ]

    operations = [
        migrations.AddField(
            model_name='introductions',
            name='brief_intro',
            field=models.CharField(default=1, max_length=128, verbose_name='简写'),
            preserve_default=False,
        ),
    ]
