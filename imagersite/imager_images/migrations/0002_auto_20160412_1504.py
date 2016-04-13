# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-12 15:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('imager_images', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='cover',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='albums_covered', to='imager_images.Photo'),
        ),
        migrations.AlterField(
            model_name='album',
            name='photos',
            field=models.ManyToManyField(null=True, related_name='albums', to='imager_images.Photo'),
        ),
    ]