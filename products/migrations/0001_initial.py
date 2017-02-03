# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=100)),
                ('description', models.CharField(default=b'', max_length=500, blank=True)),
                ('price', models.DecimalField(default=0.0, max_digits=9, decimal_places=2)),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='AreaType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', unique=True, max_length=100)),
                ('description', models.CharField(default=b'', max_length=200, blank=True)),
                ('max_guests', models.IntegerField(default=0)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cabin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', unique=True, max_length=100)),
                ('description', models.CharField(default=b'', max_length=500, blank=True)),
                ('price', models.DecimalField(default=0.0, max_digits=9, decimal_places=2)),
                ('img_url', models.CharField(default=b'http://i.imgur.com/0i6g2kx.png', max_length=500)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='CabinType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', unique=True, max_length=100)),
                ('description', models.CharField(default=b'', max_length=500, blank=True)),
                ('rooms', models.IntegerField(default=0)),
                ('max_guests', models.IntegerField(default=0)),
                ('max_extra_guests', models.IntegerField(default=0)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pool',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', unique=True, max_length=100)),
                ('description', models.CharField(default=b'', max_length=500, blank=True)),
                ('max_people', models.IntegerField(default=0, blank=True)),
                ('price', models.DecimalField(default=0.0, max_digits=9, decimal_places=2)),
                ('img_url', models.CharField(default=b'http://i.imgur.com/0i6g2kx.png', max_length=500, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='cabin',
            name='cabin_type',
            field=models.ForeignKey(to='products.CabinType'),
        ),
        migrations.AddField(
            model_name='cabin',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='area',
            name='area_type',
            field=models.ForeignKey(to='products.AreaType'),
        ),
        migrations.AddField(
            model_name='area',
            name='pools',
            field=models.ManyToManyField(to='products.Pool'),
        ),
        migrations.AddField(
            model_name='area',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
