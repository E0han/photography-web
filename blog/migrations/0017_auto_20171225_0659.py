# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-25 06:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20171222_1657'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=16, verbose_name='title')),
                ('content', models.TextField(blank=True, verbose_name='content')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ArticleTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(choices=[('zh-hans', '中文简体'), ('zh-hant', '中文繁體')], max_length=16)),
                ('title', models.CharField(max_length=16, verbose_name='title')),
                ('content', models.TextField(blank=True, verbose_name='content')),
                ('article_instance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Article', verbose_name='article')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='translations',
            field=models.ManyToManyField(blank=True, to='blog.ArticleTranslation', verbose_name='translations'),
        ),
    ]
