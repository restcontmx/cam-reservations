# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0005_auto_20170129_0206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='date_end',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='date_start',
            field=models.DateTimeField(blank=True),
        ),
    ]
