# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40, verbose_name=b'\xe5\x90\x8d\xe5\xad\x97')),
                ('address', models.CharField(max_length=60, verbose_name=b'\xe5\x9c\xb0\xe5\x9d\x80')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
