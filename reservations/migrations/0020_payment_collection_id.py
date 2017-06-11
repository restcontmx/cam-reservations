# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0019_auto_20170608_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='collection_id',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
    ]
