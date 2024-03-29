# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-25 15:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0003_auto_20161119_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(null=True, upload_to='user/avatars'),
        ),
        migrations.AddField(
            model_name='user',
            name='discription',
            field=models.TextField(default=0, max_length=4096),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default='619195275@qq.com', max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='face1',
            field=models.ImageField(null=True, upload_to='user/faces/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='face2',
            field=models.ImageField(null=True, upload_to='user/faces/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='face3',
            field=models.ImageField(null=True, upload_to='user/faces/'),
        ),
    ]
