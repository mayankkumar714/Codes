# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-07 06:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0003_auto_20170307_0633'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='profile_pic',
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='picture',
            field=models.ImageField(blank=True, upload_to='profile_pics'),
        ),
    ]