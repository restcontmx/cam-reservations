# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0013_auto_20170314_0630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentstatus',
            name='value',
            field=models.IntegerField(default=0, unique=True),
        ),
    ]
