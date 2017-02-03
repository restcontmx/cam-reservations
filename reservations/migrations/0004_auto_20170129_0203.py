# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0003_auto_20170128_0006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='date_end',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 29, 2, 3, 34, 687466), blank=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='date_start',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 29, 2, 3, 34, 687412), blank=True),
        ),
    ]
