# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-24 06:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audio_url', models.TextField()),
                ('genre', models.CharField(max_length=20)),
                ('duration', models.TimeField()),
                ('release_date', models.DateField()),
                ('language', models.CharField(max_length=10)),
                ('title', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('email_id', models.EmailField(max_length=30)),
                ('ph_num', models.IntegerField()),
                ('username', models.CharField(max_length=20)),
                ('profile_pic', models.TextField()),
                ('location', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=2)),
                ('dob', models.DateField()),
                ('verified', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='song',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.User'),
        ),
    ]
