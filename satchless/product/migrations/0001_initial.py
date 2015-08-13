# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subtype_attr', models.CharField(max_length=500, editable=False)),
                ('slug', models.SlugField(help_text='Slug will be used in the address of the product page. It should be URL-friendly (letters, numbers, hyphens and underscores only) and descriptive for the SEO needs.', unique=True, max_length=80, verbose_name='slug')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subtype_attr', models.CharField(max_length=500, editable=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
