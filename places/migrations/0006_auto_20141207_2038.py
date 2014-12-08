# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_auto_20141207_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='score',
            field=models.FloatField(max_length=40, verbose_name=b'\xe8\xaf\x84\xe5\x88\x86'),
            preserve_default=True,
        ),
    ]
