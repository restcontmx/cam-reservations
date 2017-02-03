# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0003_auto_20170124_0128'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('qty', models.IntegerField(default=0, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('total', models.DecimalField(default=0.0, max_digits=9, decimal_places=2)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=100)),
                ('description', models.CharField(default=b'', max_length=500, blank=True)),
                ('value', models.IntegerField(default=0)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=100)),
                ('description', models.CharField(default=b'', max_length=500, blank=True)),
                ('date_start', models.DateField()),
                ('date_end', models.DateField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ReservationInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('full_name', models.CharField(max_length=500, blank=True)),
                ('address1', models.CharField(max_length=500, blank=True)),
                ('address2', models.CharField(max_length=500, blank=True)),
                ('zip_code', models.IntegerField(default=0, blank=True)),
                ('city', models.CharField(max_length=100, blank=True)),
                ('state', models.CharField(max_length=100, blank=True)),
                ('country', models.CharField(max_length=100, blank=True)),
                ('email', models.EmailField(default=b'', unique=True, max_length=500, blank=True)),
                ('phone_number', models.CharField(default=b'', max_length=200, blank=True, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b'N\xc3\xbamero de tel\xc3\xa9fono incorrecto.')])),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ReservationType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=100)),
                ('description', models.CharField(default=b'', max_length=200, blank=True)),
                ('value', models.IntegerField(default=0, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DetailArea',
            fields=[
                ('detail_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='reservations.Detail')),
                ('product', models.ForeignKey(to='products.Area')),
            ],
            bases=('reservations.detail',),
        ),
        migrations.CreateModel(
            name='DetailCabin',
            fields=[
                ('detail_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='reservations.Detail')),
                ('product', models.ForeignKey(to='products.Cabin')),
            ],
            bases=('reservations.detail',),
        ),
        migrations.CreateModel(
            name='DetailPool',
            fields=[
                ('detail_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='reservations.Detail')),
                ('product', models.ForeignKey(to='products.Pool')),
            ],
            bases=('reservations.detail',),
        ),
        migrations.AddField(
            model_name='reservation',
            name='details',
            field=models.ManyToManyField(to='reservations.Detail'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='reservation_info',
            field=models.ForeignKey(to='reservations.ReservationInfo', blank=True),
        ),
        migrations.AddField(
            model_name='reservation',
            name='reservation_type',
            field=models.ForeignKey(to='reservations.ReservationType'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='user',
            field=models.ForeignKey(related_name='user_creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='reservation',
            name='user_client',
            field=models.ForeignKey(related_name='client_user', blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='payment',
            name='payment_status',
            field=models.ForeignKey(to='reservations.PaymentStatus'),
        ),
        migrations.AddField(
            model_name='payment',
            name='promotion',
            field=models.ForeignKey(to='reservations.Promotion'),
        ),
        migrations.AddField(
            model_name='payment',
            name='reservation',
            field=models.ForeignKey(to='reservations.Reservation'),
        ),
        migrations.AddField(
            model_name='payment',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='detail',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
