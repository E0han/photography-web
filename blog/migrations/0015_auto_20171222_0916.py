# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-22 09:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20171222_0914'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gallery',
            old_name='title_gallery',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='gallery_name',
            new_name='gallery',
        ),
    ]
