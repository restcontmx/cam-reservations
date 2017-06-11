# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0012_reservationcabin_extended_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservationcabin',
            name='payment_status',
            field=models.ForeignKey(default=1, to='reservations.PaymentStatus', null=True),
        ),
        migrations.AlterField(
            model_name='reservationinfo',
            name='address1',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='reservationinfo',
            name='address2',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='reservationinfo',
            name='email',
            field=models.EmailField(default=b'', max_length=500),
        ),
        migrations.AlterField(
            model_name='reservationinfo',
            name='full_name',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='reservationinfo',
            name='phone_number',
            field=models.CharField(default=b'', max_length=200, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b'N\xc3\xbamero de tel\xc3\xa9fono incorrecto.')]),
        ),
        migrations.AlterField(
            model_name='reservationinfo',
            name='zip_code',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
    ]
