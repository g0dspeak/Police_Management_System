# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-09 18:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('house_no', models.TextField()),
                ('locality', models.TextField()),
                ('city', models.TextField()),
                ('state', models.TextField()),
                ('pin_code', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Police',
            fields=[
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('salary', models.IntegerField()),
                ('description', models.TextField()),
                ('post', models.CharField(default='Inspector', max_length=30)),
                ('rank', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User_profile',
            fields=[
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone_no', models.IntegerField()),
                ('isPolice', models.BooleanField(default=False)),
                ('age', models.IntegerField()),
            ],
        ),
    ]