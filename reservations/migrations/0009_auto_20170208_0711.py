# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0008_auto_20170208_0657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='details',
            field=models.ManyToManyField(to='reservations.Detail', null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='max_guests',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='user_client',
            field=models.ForeignKey(related_name='client_user', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
