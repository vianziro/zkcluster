# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-12 10:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('status', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DeletedUID',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Terminal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('serialnumber', models.CharField(max_length=100, unique=True, verbose_name='serialnumber')),
                ('ip', models.CharField(max_length=15, unique=True, verbose_name='ip')),
                ('port', models.IntegerField(default=4370, verbose_name='port')),
            ],
        ),
        migrations.CreateModel(
            name='UIDCounter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('next_uid', models.IntegerField()),
                ('terminal', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='counter', to='zkcluster.Terminal')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField(verbose_name='uid')),
                ('name', models.CharField(max_length=28, verbose_name='name')),
                ('privilege', models.SmallIntegerField(choices=[(0, 'User'), (14, 'Administrator')], default=0, verbose_name='privilege')),
                ('password', models.CharField(blank=True, max_length=8, null=True, verbose_name='password')),
                ('group_id', models.CharField(blank=True, max_length=7, null=True, verbose_name='group id')),
                ('terminal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users', to='zkcluster.Terminal')),
            ],
        ),
        migrations.AddField(
            model_name='deleteduid',
            name='terminal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deleted_uids', to='zkcluster.Terminal'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendances', to='zkcluster.User'),
        ),
        migrations.AlterUniqueTogether(
            name='user',
            unique_together=set([('uid', 'terminal')]),
        ),
    ]
