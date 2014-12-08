# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_auto_20141207_2038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='recommandTime',
        ),
        migrations.AddField(
            model_name='place',
            name='recommendTime',
            field=models.FloatField(default=1, max_length=40, verbose_name=b'\xe6\x8e\xa8\xe8\x8d\x90\xe6\x97\xb6\xe9\x95\xbf'),
            preserve_default=False,
        ),
    ]
