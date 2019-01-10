# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-01-10 11:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20180907_1920'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('product_description', models.CharField(max_length=200)),
                ('product_image', models.ImageField(upload_to='photos')),
                ('remain_product', models.IntegerField(default=0)),
            ],
        ),
    ]