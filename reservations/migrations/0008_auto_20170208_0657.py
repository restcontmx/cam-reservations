# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0007_auto_20170208_0505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservationinfo',
            name='email',
            field=models.EmailField(default=b'', max_length=500, blank=True),
        ),
    ]
