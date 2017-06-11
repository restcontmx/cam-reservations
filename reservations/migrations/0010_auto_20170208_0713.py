# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0009_auto_20170208_0711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='details',
            field=models.ManyToManyField(to='reservations.Detail'),
        ),
    ]
