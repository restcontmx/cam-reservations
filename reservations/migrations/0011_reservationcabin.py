# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reservations', '0010_auto_20170208_0713'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReservationCabin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('max_guests', models.IntegerField(default=0, null=True)),
                ('extra_guests_child', models.IntegerField(default=0)),
                ('extra_guests_adult', models.IntegerField(default=0)),
                ('total', models.DecimalField(default=0.0, max_digits=9, decimal_places=2)),
                ('date_start', models.DateTimeField(null=True, blank=True)),
                ('date_end', models.DateTimeField(null=True, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('details', models.ManyToManyField(to='reservations.DetailCabin')),
                ('reservation_info', models.ForeignKey(to='reservations.ReservationInfo', null=True)),
                ('user', models.ForeignKey(related_name='user_creator_rescab', to=settings.AUTH_USER_MODEL)),
                ('user_client', models.ForeignKey(related_name='client_user_rescab', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
    ]
