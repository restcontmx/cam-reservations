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
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=500)),
                ('description', models.CharField(default=b'', max_length=500, blank=True)),
                ('date_end', models.DateTimeField()),
                ('value', models.IntegerField(default=0, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(related_name='master', to=settings.AUTH_USER_MODEL)),
                ('user_assigned', models.ForeignKey(related_name='assigned_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
