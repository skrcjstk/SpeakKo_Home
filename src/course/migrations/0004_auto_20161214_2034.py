# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-14 11:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_auto_20161214_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='class_category',
            field=models.CharField(max_length=50),
        ),
    ]
