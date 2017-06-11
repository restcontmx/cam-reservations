# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0014_auto_20170314_0658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservationcabin',
            name='payment_status',
            field=models.ForeignKey(default=2, to='reservations.PaymentStatus', null=True),
        ),
    ]
