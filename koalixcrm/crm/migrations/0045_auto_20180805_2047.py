# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-08-05 20:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0044_reportingperiod_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='worked_hours',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Stop Time'),
        ),
        migrations.AlterField(
            model_name='task',
            name='planned_end_date',
            field=models.DateField(blank=True, null=True, verbose_name='Planned End'),
        ),
        migrations.AlterField(
            model_name='task',
            name='planned_start_date',
            field=models.DateField(blank=True, null=True, verbose_name='Planned Start'),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.TaskStatus', verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='work',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Start Time'),
        ),
        migrations.AlterField(
            model_name='work',
            name='stop_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Stop Time'),
        ),
    ]