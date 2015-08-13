# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import satchless.cart.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('typ', models.CharField(max_length=100, verbose_name='type')),
                ('currency', models.CharField(default=satchless.cart.models.get_default_currency, max_length=3, verbose_name='currency')),
                ('owner', models.ForeignKey(related_name='carts', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
    ]
