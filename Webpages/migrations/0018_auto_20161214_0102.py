# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-12-14 01:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Webpages', '0017_auto_20161213_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='upload_time',
            field=models.DateTimeField(auto_now=True, verbose_name='\u4e0a\u4f20\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='picture',
            name='upload_time',
            field=models.DateTimeField(auto_now=True, verbose_name='\u4e0a\u4f20\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='video',
            name='upload_time',
            field=models.DateTimeField(auto_now=True, verbose_name='\u4e0a\u4f20\u65f6\u95f4'),
        ),
    ]
