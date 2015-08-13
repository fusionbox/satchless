# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryVariant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subtype_attr', models.CharField(max_length=500, editable=False)),
                ('name', models.CharField(max_length=128, verbose_name='name')),
                ('description', models.TextField(verbose_name='description', blank=True)),
                ('price', models.DecimalField(verbose_name='unit price', max_digits=12, decimal_places=4)),
                ('delivery_group', models.OneToOneField(to='order.DeliveryGroup')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
