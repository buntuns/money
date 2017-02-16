# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-15 09:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gold', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='outcome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('income_text', models.CharField(max_length=200)),
                ('money_in_text', models.CharField(max_length=20)),
                ('expenses_text', models.CharField(max_length=200)),
                ('money_out_text', models.CharField(max_length=20)),
            ],
        ),
    ]