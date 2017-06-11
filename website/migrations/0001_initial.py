# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OurCompanyContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=500, null=True)),
                ('content', models.CharField(default=b'', max_length=1000, null=True)),
                ('img_url_1', models.CharField(default=b'http://i.imgur.com/0i6g2kx.png', max_length=500)),
                ('img_url_2', models.CharField(default=b'http://i.imgur.com/0i6g2kx.png', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='OurPersonalContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(default=b'', max_length=1000, null=True)),
                ('img_url', models.CharField(default=b'http://i.imgur.com/0i6g2kx.png', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='OurProductsContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price_range', models.CharField(default=b'', max_length=100, null=True)),
                ('product_name', models.CharField(default=b'', max_length=100, null=True)),
                ('content', models.CharField(default=b'', max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OurServicesContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('icon', models.CharField(default=b'', max_length=50, null=True)),
                ('title', models.CharField(default=b'', max_length=500, null=True)),
                ('content', models.CharField(default=b'', max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recomendations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(default=b'', max_length=1000, null=True)),
                ('source', models.CharField(default=b'', max_length=500, null=True)),
            ],
        ),
    ]
