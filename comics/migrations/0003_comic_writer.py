# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-02-09 20:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comics', '0002_comic_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='comic',
            name='writer',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
