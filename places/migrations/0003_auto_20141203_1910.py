# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_auto_20141130_0314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='address',
            field=models.TextField(verbose_name=b'\xe5\x9c\xb0\xe5\x9d\x80'),
            preserve_default=True,
        ),
    ]
