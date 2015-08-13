# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('product', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('delivery_type', models.CharField(max_length=256, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(default=b'checkout', max_length=32, verbose_name='order status', choices=[(b'checkout', 'undergoing checkout'), (b'payment-pending', 'waiting for payment'), (b'payment-complete', 'paid'), (b'payment-failed', 'payment failed'), (b'delivery', 'shipped'), (b'cancelled', 'cancelled')])),
                ('created', models.DateTimeField(default=datetime.datetime.now, editable=False, blank=True)),
                ('last_status_change', models.DateTimeField(default=datetime.datetime.now, editable=False, blank=True)),
                ('currency', models.CharField(max_length=3)),
                ('billing_first_name', models.CharField(max_length=256, verbose_name='first name', blank=True)),
                ('billing_last_name', models.CharField(max_length=256, verbose_name='last name', blank=True)),
                ('billing_company_name', models.CharField(max_length=256, verbose_name='company name', blank=True)),
                ('billing_street_address_1', models.CharField(max_length=256, verbose_name='street address 1', blank=True)),
                ('billing_street_address_2', models.CharField(max_length=256, verbose_name='street address 2', blank=True)),
                ('billing_city', models.CharField(max_length=256, verbose_name='city', blank=True)),
                ('billing_postal_code', models.CharField(max_length=20, verbose_name='postal code', blank=True)),
                ('billing_country', models.CharField(blank=True, max_length=2, verbose_name='country', choices=[(b'AF', 'Afghanistan'), (b'AX', '\xc5land Islands'), (b'AL', 'Albania'), (b'DZ', 'Algeria'), (b'AS', 'American Samoa'), (b'AD', 'Andorra'), (b'AO', 'Angola'), (b'AI', 'Anguilla'), (b'AQ', 'Antarctica'), (b'AG', 'Antigua And Barbuda'), (b'AR', 'Argentina'), (b'AM', 'Armenia'), (b'AW', 'Aruba'), (b'AU', 'Australia'), (b'AT', 'Austria'), (b'AZ', 'Azerbaijan'), (b'BS', 'Bahamas'), (b'BH', 'Bahrain'), (b'BD', 'Bangladesh'), (b'BB', 'Barbados'), (b'BY', 'Belarus'), (b'BE', 'Belgium'), (b'BZ', 'Belize'), (b'BJ', 'Benin'), (b'BM', 'Bermuda'), (b'BT', 'Bhutan'), (b'BO', 'Bolivia'), (b'BQ', 'Bonaire, Saint Eustatius And Saba'), (b'BA', 'Bosnia And Herzegovina'), (b'BW', 'Botswana'), (b'BV', 'Bouvet Island'), (b'BR', 'Brazil'), (b'IO', 'British Indian Ocean Territory'), (b'BN', 'Brunei Darussalam'), (b'BG', 'Bulgaria'), (b'BF', 'Burkina Faso'), (b'BI', 'Burundi'), (b'KH', 'Cambodia'), (b'CM', 'Cameroon'), (b'CA', 'Canada'), (b'CV', 'Cape Verde'), (b'KY', 'Cayman Islands'), (b'CF', 'Central African Republic'), (b'TD', 'Chad'), (b'CL', 'Chile'), (b'CN', 'China'), (b'CX', 'Christmas Island'), (b'CC', 'Cocos (Keeling) Islands'), (b'CO', 'Colombia'), (b'KM', 'Comoros'), (b'CG', 'Congo'), (b'CD', 'Congo, The Democratic Republic of the'), (b'CK', 'Cook Islands'), (b'CR', 'Costa Rica'), (b'CI', "C\xf4te D'Ivoire"), (b'HR', 'Croatia'), (b'CU', 'Cuba'), (b'CW', 'Cura\xe7o'), (b'CY', 'Cyprus'), (b'CZ', 'Czech Republic'), (b'DK', 'Denmark'), (b'DJ', 'Djibouti'), (b'DM', 'Dominica'), (b'DO', 'Dominican Republic'), (b'EC', 'Ecuador'), (b'EG', 'Egypt'), (b'SV', 'El Salvador'), (b'GQ', 'Equatorial Guinea'), (b'ER', 'Eritrea'), (b'EE', 'Estonia'), (b'ET', 'Ethiopia'), (b'FK', 'Falkland Islands (Malvinas)'), (b'FO', 'Faroe Islands'), (b'FJ', 'Fiji'), (b'FI', 'Finland'), (b'FR', 'France'), (b'GF', 'French Guiana'), (b'PF', 'French Polynesia'), (b'TF', 'French Southern Territories'), (b'GA', 'Gabon'), (b'GM', 'Gambia'), (b'GE', 'Georgia'), (b'DE', 'Germany'), (b'GH', 'Ghana'), (b'GI', 'Gibraltar'), (b'GR', 'Greece'), (b'GL', 'Greenland'), (b'GD', 'Grenada'), (b'GP', 'Guadeloupe'), (b'GU', 'Guam'), (b'GT', 'Guatemala'), (b'GG', 'Guernsey'), (b'GN', 'Guinea'), (b'GW', 'Guinea-Bissau'), (b'GY', 'Guyana'), (b'HT', 'Haiti'), (b'HM', 'Heard Island And Mcdonald Islands'), (b'VA', 'Holy See (Vatican City State)'), (b'HN', 'Honduras'), (b'HK', 'Hong Kong'), (b'HU', 'Hungary'), (b'IS', 'Iceland'), (b'IN', 'India'), (b'ID', 'Indonesia'), (b'IR', 'Iran, Islamic Republic of'), (b'IQ', 'Iraq'), (b'IE', 'Ireland'), (b'IM', 'Isle of Man'), (b'IL', 'Israel'), (b'IT', 'Italy'), (b'JM', 'Jamaica'), (b'JP', 'Japan'), (b'JE', 'Jersey'), (b'JO', 'Jordan'), (b'KZ', 'Kazakhstan'), (b'KE', 'Kenya'), (b'KI', 'Kiribati'), (b'KP', "Korea, Democratic People's Republic of"), (b'KR', 'Korea, Republic of'), (b'KW', 'Kuwait'), (b'KG', 'Kyrgyzstan'), (b'LA', "Lao People's Democratic Republic"), (b'LV', 'Latvia'), (b'LB', 'Lebanon'), (b'LS', 'Lesotho'), (b'LR', 'Liberia'), (b'LY', 'Libya'), (b'LI', 'Liechtenstein'), (b'LT', 'Lithuania'), (b'LU', 'Luxembourg'), (b'MO', 'Macao'), (b'MK', 'Macedonia, The Former Yugoslav Republic of'), (b'MG', 'Madagascar'), (b'MW', 'Malawi'), (b'MY', 'Malaysia'), (b'MV', 'Maldives'), (b'ML', 'Mali'), (b'MT', 'Malta'), (b'MH', 'Marshall Islands'), (b'MQ', 'Martinique'), (b'MR', 'Mauritania'), (b'MU', 'Mauritius'), (b'YT', 'Mayotte'), (b'MX', 'Mexico'), (b'FM', 'Micronesia, Federated States of'), (b'MD', 'Moldova, Republic of'), (b'MC', 'Monaco'), (b'MN', 'Mongolia'), (b'ME', 'Montenegro'), (b'MS', 'Montserrat'), (b'MA', 'Morocco'), (b'MZ', 'Mozambique'), (b'MM', 'Myanmar'), (b'NA', 'Namibia'), (b'NR', 'Nauru'), (b'NP', 'Nepal'), (b'NL', 'Netherlands'), (b'NC', 'New Caledonia'), (b'NZ', 'New Zealand'), (b'NI', 'Nicaragua'), (b'NE', 'Niger'), (b'NG', 'Nigeria'), (b'NU', 'Niue'), (b'NF', 'Norfolk Island'), (b'MP', 'Northern Mariana Islands'), (b'NO', 'Norway'), (b'OM', 'Oman'), (b'PK', 'Pakistan'), (b'PW', 'Palau'), (b'PS', 'Palestinian Territory, Occupied'), (b'PA', 'Panama'), (b'PG', 'Papua New Guinea'), (b'PY', 'Paraguay'), (b'PE', 'Peru'), (b'PH', 'Philippines'), (b'PN', 'Pitcairn'), (b'PL', 'Poland'), (b'PT', 'Portugal'), (b'PR', 'Puerto Rico'), (b'QA', 'Qatar'), (b'RE', 'R\xe9union'), (b'RO', 'Romania'), (b'RU', 'Russian Federation'), (b'RW', 'Rwanda'), (b'BL', 'Saint Barth\xe9lemy'), (b'SH', 'Saint Helena, Ascension And Tristan Da Cunha'), (b'KN', 'Saint Kitts And Nevis'), (b'LC', 'Saint Lucia'), (b'MF', 'Saint Martin (French Part)'), (b'PM', 'Saint Pierre And Miquelon'), (b'VC', 'Saint Vincent And the Grenadines'), (b'WS', 'Samoa'), (b'SM', 'San Marino'), (b'ST', 'Sao Tome And Principe'), (b'SA', 'Saudi Arabia'), (b'SN', 'Senegal'), (b'RS', 'Serbia'), (b'SC', 'Seychelles'), (b'SL', 'Sierra Leone'), (b'SG', 'Singapore'), (b'SX', 'Sint Maarten (Dutch Part)'), (b'SK', 'Slovakia'), (b'SI', 'Slovenia'), (b'SB', 'Solomon Islands'), (b'SO', 'Somalia'), (b'ZA', 'South Africa'), (b'GS', 'South Georgia and the South Sandwich Islands'), (b'ES', 'Spain'), (b'LK', 'Sri Lanka'), (b'SD', 'Sudan'), (b'SR', 'Suriname'), (b'SJ', 'Svalbard and Jan Mayen'), (b'SZ', 'Swaziland'), (b'SE', 'Sweden'), (b'CH', 'Switzerland'), (b'SY', 'Syria'), (b'TW', 'Taiwan'), (b'TJ', 'Tajikistan'), (b'TZ', 'Tanzania'), (b'TH', 'Thailand'), (b'TL', 'Timor-Leste'), (b'TG', 'Togo'), (b'TK', 'Tokelau'), (b'TO', 'Tonga'), (b'TT', 'Trinidad And Tobago'), (b'TN', 'Tunisia'), (b'TR', 'Turkey'), (b'TM', 'Turkmenistan'), (b'TC', 'Turks And Caicos Islands'), (b'TV', 'Tuvalu'), (b'UG', 'Uganda'), (b'UA', 'Ukraine'), (b'AE', 'United Arab Emirates'), (b'GB', 'United Kingdom'), (b'US', 'United States'), (b'UM', 'United States Minor Outlying Islands'), (b'UY', 'Uruguay'), (b'UZ', 'Uzbekistan'), (b'VU', 'Vanuatu'), (b'VE', 'Venezuela'), (b'VN', 'Viet Nam'), (b'VG', 'Virgin Islands, British'), (b'VI', 'Virgin Islands, U.S.'), (b'WF', 'Wallis And Futuna'), (b'EH', 'Western Sahara'), (b'YE', 'Yemen'), (b'ZM', 'Zambia'), (b'ZW', 'Zimbabwe')])),
                ('billing_country_area', models.CharField(max_length=128, verbose_name='country administrative area', blank=True)),
                ('billing_tax_id', models.CharField(max_length=40, verbose_name='tax ID', blank=True)),
                ('billing_phone', models.CharField(max_length=30, verbose_name='phone number', blank=True)),
                ('payment_type', models.CharField(max_length=256, blank=True)),
                ('token', models.CharField(default=b'', max_length=32, blank=True)),
                ('user', models.ForeignKey(related_name='orders', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-last_status_change',),
                'verbose_name': 'order (business)',
                'verbose_name_plural': 'orders (business)',
            },
        ),
        migrations.CreateModel(
            name='OrderedItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_name', models.CharField(max_length=128)),
                ('quantity', models.DecimalField(verbose_name='quantity', max_digits=10, decimal_places=4)),
                ('unit_price_net', models.DecimalField(verbose_name='unit price (net)', max_digits=12, decimal_places=4)),
                ('unit_price_gross', models.DecimalField(verbose_name='unit price (gross)', max_digits=12, decimal_places=4)),
                ('delivery_group', models.ForeignKey(related_name='items', to='order.DeliveryGroup')),
                ('product_variant', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='product.Variant', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='deliverygroup',
            name='order',
            field=models.ForeignKey(related_name='groups', to='order.Order'),
        ),
    ]
