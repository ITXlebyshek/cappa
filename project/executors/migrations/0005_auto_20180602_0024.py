# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-01 19:24
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('executors', '0004_auto_20180527_1423'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSolution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', django.contrib.postgres.fields.jsonb.JSONField(default={'best_solution_tests': [], 'solutions': []}, verbose_name='детали решения')),
                ('progress', models.PositiveIntegerField(default=0, verbose_name='Прогресс решения')),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='executors.Code', verbose_name='блок кода')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'пользовательское решение',
                'verbose_name_plural': 'пользовательские решения',
            },
        ),
        migrations.RemoveField(
            model_name='codesolution',
            name='code',
        ),
        migrations.RemoveField(
            model_name='codesolution',
            name='user',
        ),
        migrations.DeleteModel(
            name='CodeSolution',
        ),
    ]