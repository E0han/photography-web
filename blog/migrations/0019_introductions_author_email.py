# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-25 07:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20171225_0702'),
    ]

    operations = [
        migrations.AddField(
            model_name='introductions',
            name='author_email',
            field=models.CharField(default=1, max_length=256, verbose_name='作者邮箱'),
            preserve_default=False,
        ),
    ]
