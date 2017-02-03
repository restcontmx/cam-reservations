# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20170123_0337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='pools',
            field=models.ManyToManyField(to='products.Pool', blank=True),
        ),
    ]
