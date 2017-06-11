# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0018_payment_preference_mp_init_point'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_status',
            field=models.ForeignKey(default=3, to='reservations.PaymentStatus', null=True),
        ),
    ]
