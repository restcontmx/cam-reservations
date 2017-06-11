# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0011_reservationcabin'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservationcabin',
            name='extended_token',
            field=models.CharField(default=uuid.uuid4, unique=True, max_length=100, blank=True),
        ),
    ]
