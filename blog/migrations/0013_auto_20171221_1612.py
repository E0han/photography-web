# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-21 16:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20171221_1507'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='gallery',
            new_name='gallery_name',
        ),
    ]
