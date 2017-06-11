# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0006_auto_20170131_0302'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='extra_guests_adult',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='reservation',
            name='extra_guests_child',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='reservation',
            name='max_guests',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='reservation',
            name='total',
            field=models.DecimalField(default=0.0, max_digits=9, decimal_places=2),
        ),
    ]
