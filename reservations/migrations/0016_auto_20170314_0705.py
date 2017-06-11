# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0015_auto_20170314_0659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservationcabin',
            name='payment_status',
            field=models.ForeignKey(default=3, to='reservations.PaymentStatus', null=True),
        ),
    ]
