# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-10-14 09:20
# Manually modified to serve as input for the data migration 0009_migrate_to_datetimes
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wafer.snippets.markdown_field


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0007_venue_add_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduleBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ['start_time'],
            },
        ),
        migrations.AlterModelOptions(
            name='slot',
            options={'ordering': ['end_time', 'start_time']},
        ),
        migrations.RenameField(
            model_name='slot',
            old_name='start_time',
            new_name='old_start_time',
        ),
        migrations.RenameField(
            model_name='slot',
            old_name='end_time',
            new_name='old_end_time',
        ),
        migrations.AddField(
            model_name='slot',
            name='end_time',
            field=models.DateTimeField(help_text='Slot end time', null=True),
        ),
        migrations.AddField(
            model_name='slot',
            name='start_time',
            field=models.DateTimeField(blank=True, help_text='Start time (if no previous slot selected)', null=True),
        ),
        migrations.AlterField(
            model_name='slot',
            name='previous_slot',
            field=models.ForeignKey(blank=True, help_text='Previous slot if applicable (slots should have either a previous slot OR a start time set)',
                                    null=True, on_delete=django.db.models.deletion.CASCADE, to='schedule.Slot'),
        ),
        migrations.AddField(
            model_name='venue',
            name='blocks',
            field=models.ManyToManyField(help_text='Blocks (days) on which this venue will be used.', to='schedule.ScheduleBlock'),
        ),
    ]
