# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-21 14:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20171207_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='gallery',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='image', to='blog.Gallery'),
        ),
    ]
