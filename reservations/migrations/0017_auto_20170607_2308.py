# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0016_auto_20170314_0705'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='promotion',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='reservation',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='total',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='user',
        ),
        migrations.AddField(
            model_name='payment',
            name='preference_mp_id',
            field=models.CharField(default=b'', max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='reservationcabin',
            name='payment_info',
            field=models.ForeignKey(blank=True, to='reservations.Payment', null=True),
        ),
    ]
