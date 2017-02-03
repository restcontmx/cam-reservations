# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0002_promotion_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='date_end',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 28, 0, 6, 45, 697256), blank=True),
        ),
        migrations.AddField(
            model_name='reservation',
            name='date_start',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 28, 0, 6, 45, 697226), blank=True),
        ),
    ]
