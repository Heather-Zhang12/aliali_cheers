# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-12-13 00:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Webpages', '0016_auto_20161212_1552'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='three_gp',
            new_name='low_ppi',
        ),
    ]
