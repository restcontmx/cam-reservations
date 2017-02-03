# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='promotion',
            name='discount',
            field=models.DecimalField(default=0.0, max_digits=9, decimal_places=2, blank=True),
        ),
    ]
