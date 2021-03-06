# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-21 15:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20171221_1503'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='title',
            field=models.CharField(default=1, max_length=20, verbose_name='Title'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='image',
            name='gallery',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Gallery'),
        ),
    ]
