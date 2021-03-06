# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-01 03:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190131_0214'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 1, 3, 47, 28, 294645, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 1, 3, 47, 28, 293216, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='like',
            name='number',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='blog.Post'),
        ),
    ]
