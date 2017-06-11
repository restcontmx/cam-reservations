# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0017_auto_20170607_2308'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='preference_mp_init_point',
            field=models.CharField(default=b'', max_length=256, null=True, blank=True),
        ),
    ]
