# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlertEmails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=100)),
                ('email', models.EmailField(default=b'', max_length=500, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='AlertNumbers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=100)),
                ('phone_number', models.CharField(default=b'', max_length=200, blank=True, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b'N\xc3\xbamero de tel\xc3\xa9fono incorrecto.')])),
            ],
        ),
        migrations.CreateModel(
            name='ContactEmail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=100)),
                ('email', models.EmailField(default=b'', max_length=500, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Signatures',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=100)),
                ('img_url', models.CharField(default=b'http://i.imgur.com/0i6g2kx.png', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='TicketPrices',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=100)),
                ('price', models.DecimalField(default=0.0, max_digits=9, decimal_places=2)),
            ],
        ),
    ]
