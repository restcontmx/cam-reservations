# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0004_auto_20170129_0203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='date_end',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 29, 2, 6, 28, 91623), blank=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='date_start',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 29, 2, 6, 28, 91587), blank=True),
        ),
    ]
