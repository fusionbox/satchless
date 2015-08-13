# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PriceQtyOverride',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('min_qty', models.DecimalField(verbose_name='minimal quantity', max_digits=10, decimal_places=4)),
                ('price', models.DecimalField(verbose_name='unit price', max_digits=12, decimal_places=4)),
            ],
            options={
                'ordering': ('min_qty',),
            },
        ),
        migrations.CreateModel(
            name='ProductPrice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('qty_mode', models.CharField(default=b'variant', help_text="In 'per variant' mode the unit price will depend on quantity of single variant being sold. In 'per product' mode, total quantity of all product's variants will be used.", max_length=10, verbose_name='Quantity pricing mode', choices=[(b'product', 'per product'), (b'variant', 'per variant')])),
                ('price', models.DecimalField(verbose_name='base price', max_digits=12, decimal_places=4)),
                ('product', models.OneToOneField(to='product.Product')),
            ],
        ),
        migrations.CreateModel(
            name='VariantPriceOffset',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price_offset', models.DecimalField(verbose_name='unit price offset', max_digits=12, decimal_places=4)),
                ('base_price', models.ForeignKey(related_name='offsets', to='simpleqty.ProductPrice')),
                ('variant', models.OneToOneField(to='product.Variant')),
            ],
        ),
        migrations.AddField(
            model_name='priceqtyoverride',
            name='base_price',
            field=models.ForeignKey(related_name='qty_overrides', to='simpleqty.ProductPrice'),
        ),
    ]
