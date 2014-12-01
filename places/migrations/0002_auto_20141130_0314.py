# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='experience',
            field=models.TextField(default=1, verbose_name=b'\xe7\xbd\x91\xe5\x8f\x8b\xe7\xbb\x8f\xe9\xaa\x8c'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='place',
            name='intro',
            field=models.TextField(default=1, verbose_name=b'\xe6\x99\xaf\xe7\x82\xb9\xe4\xbb\x8b\xe7\xbb\x8d'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='place',
            name='openhours',
            field=models.CharField(default=1, max_length=40, verbose_name=b'\xe5\xbc\x80\xe6\x94\xbe\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='place',
            name='recommandTime',
            field=models.CharField(default=1, max_length=40, verbose_name=b'\xe6\x8e\xa8\xe8\x8d\x90\xe6\x97\xb6\xe9\x95\xbf'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='place',
            name='score',
            field=models.CharField(default=1, max_length=40, verbose_name=b'\xe8\xaf\x84\xe5\x88\x86'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='place',
            name='ticketInfo',
            field=models.CharField(default=1, max_length=40, verbose_name=b'\xe9\x97\xa8\xe7\xa5\xa8\xe4\xbf\xa1\xe6\x81\xaf'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='place',
            name='tips',
            field=models.TextField(default=1, verbose_name=b'\xe6\x97\x85\xe8\xa1\x8c\xe5\xb0\x8f\xe8\xb4\xb4\xe5\xa3\xab'),
            preserve_default=False,
        ),
    ]
