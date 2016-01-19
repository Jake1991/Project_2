# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-18 21:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0006_dayscore'),
    ]

    operations = [
        migrations.CreateModel(
            name='SimpleQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField()),
                ('answer', models.CharField(max_length=100)),
                ('dummy_answer_a', models.CharField(max_length=100)),
                ('dummy_answer_b', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='dayscore',
            name='date',
            field=models.DateField(default=datetime.date(2016, 1, 18)),
        ),
    ]