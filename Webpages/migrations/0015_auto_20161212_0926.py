# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-12-12 09:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Webpages', '0014_auto_20161202_1502'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='bmp',
            field=models.ImageField(blank=True, upload_to='pictures/'),
        ),
        migrations.AddField(
            model_name='picture',
            name='gif',
            field=models.ImageField(blank=True, upload_to='pictures/'),
        ),
        migrations.AddField(
            model_name='picture',
            name='jpg',
            field=models.ImageField(blank=True, upload_to='pictures/'),
        ),
        migrations.AddField(
            model_name='picture',
            name='png',
            field=models.ImageField(blank=True, upload_to='pictures/'),
        ),
    ]
