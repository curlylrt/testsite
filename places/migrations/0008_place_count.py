# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0007_auto_20141208_0345'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='count',
            field=models.IntegerField(default=10, verbose_name=b'\xe6\x80\xbb\xe6\x8a\x95\xe7\xa5\xa8\xe6\x95\xb0'),
            preserve_default=False,
        ),
    ]
