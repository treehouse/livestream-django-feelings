# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 15:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0005_auto_20170203_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyinvite',
            name='status',
            field=models.IntegerField(choices=[(0, 'Pending'), (1, 'Accepted'), (2, 'Rejected')], default=0),
        ),
        migrations.AlterField(
            model_name='companyinvite',
            name='uuid',
            field=models.CharField(blank=True, default='', max_length=32),
        ),
        migrations.AlterField(
            model_name='familyinvite',
            name='status',
            field=models.IntegerField(choices=[(0, 'Pending'), (1, 'Accepted'), (2, 'Rejected')], default=0),
        ),
        migrations.AlterField(
            model_name='familyinvite',
            name='uuid',
            field=models.CharField(blank=True, default='', max_length=32),
        ),
    ]
