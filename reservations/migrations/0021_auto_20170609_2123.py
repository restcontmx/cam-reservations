# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0020_payment_collection_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='collection_id',
            field=models.BigIntegerField(default=0, null=True, blank=True),
        ),
    ]
