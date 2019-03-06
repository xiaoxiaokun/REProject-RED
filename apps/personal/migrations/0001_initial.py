# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-03-01 15:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WorkOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='标题')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('content', models.CharField(max_length=300, verbose_name='工单内容')),
            ],
            options={
                'verbose_name': '销售信息',
                'verbose_name_plural': '销售信息',
            },
        ),
    ]
