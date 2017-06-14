# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0021_auto_20170609_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_status',
            field=models.ForeignKey(default=1, to='reservations.PaymentStatus', null=True),
        ),
        migrations.AlterField(
            model_name='reservationcabin',
            name='payment_status',
            field=models.ForeignKey(default=1, to='reservations.PaymentStatus', null=True),
        ),
    ]
