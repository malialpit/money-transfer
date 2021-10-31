# Generated by Django 3.2.6 on 2021-10-06 11:02

import customeraccess.models
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('administration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receiver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_type', models.CharField(choices=[('mr', 'Mr.'), ('mrs', 'Mrs.'), ('ms', 'Ms.'), ('miss', 'Miss.'), ('dr', 'Dr.')], max_length=30, null=True)),
                ('first_name', models.CharField(max_length=100, null=True)),
                ('last_name', models.CharField(max_length=70, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('mobile_no', phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None)),
                ('city', models.CharField(max_length=50, null=True)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('account_name', models.CharField(max_length=100, null=True)),
                ('account_no', models.CharField(max_length=100, null=True)),
                ('branch_code', models.CharField(max_length=70, null=True)),
                ('bank_name', models.CharField(max_length=70, null=True)),
                ('bank_contact', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('bank_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('description', models.CharField(blank=True, max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='SendMoney',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_currency', models.CharField(blank=True, choices=[('AED', 'AED'), ('ARS', 'ARS'), ('AUD', 'AUD'), ('BGN', 'BGN'), ('BRL', 'BRL'), ('BSD', 'BSD'), ('CAD', 'CAD'), ('CHF', 'CHF'), ('CLP', 'CLP'), ('CNY', 'CNY'), ('COP', 'COP'), ('CZK', 'CZK'), ('DKK', 'DKK'), ('DOP', 'DOP'), ('EGP', 'EGP'), ('EUR', 'EUR'), ('FJD', 'FJD'), ('GBP', 'GBP'), ('GTQ', 'GTQ'), ('HKD', 'HKD'), ('HRK', 'HRK'), ('HUF', 'HUF'), ('IDR', 'IDR'), ('ILS', 'ILS'), ('INR', 'INR'), ('ISK', 'ISK'), ('JPY', 'JPY'), ('KRW', 'KRW'), ('KZT', 'KZT'), ('MXN', 'MXN'), ('MYR', 'MYR'), ('NOK', 'NOK'), ('NZD', 'NZD'), ('PAB', 'PAB'), ('PEN', 'PEN'), ('PHP', 'PHP'), ('PKR', 'PKR'), ('PLN', 'PLN'), ('PYG', 'PYG'), ('RON', 'RON'), ('RUB', 'RUB'), ('SAR', 'SAR'), ('SEK', 'SEK'), ('SAR', 'SAR'), ('SGD', 'SGD'), ('THB', 'THB'), ('TRY', 'TRY'), ('TWD', 'TWD'), ('UAH', 'UAH'), ('USD', 'USD'), ('UYU', 'UYU'), ('VND', 'VND'), ('ZAR', 'ZAR')], max_length=5, null=True)),
                ('to_currency', models.CharField(blank=True, choices=[('AED', 'AED'), ('ARS', 'ARS'), ('AUD', 'AUD'), ('BGN', 'BGN'), ('BRL', 'BRL'), ('BSD', 'BSD'), ('CAD', 'CAD'), ('CHF', 'CHF'), ('CLP', 'CLP'), ('CNY', 'CNY'), ('COP', 'COP'), ('CZK', 'CZK'), ('DKK', 'DKK'), ('DOP', 'DOP'), ('EGP', 'EGP'), ('EUR', 'EUR'), ('FJD', 'FJD'), ('GBP', 'GBP'), ('GTQ', 'GTQ'), ('HKD', 'HKD'), ('HRK', 'HRK'), ('HUF', 'HUF'), ('IDR', 'IDR'), ('ILS', 'ILS'), ('INR', 'INR'), ('ISK', 'ISK'), ('JPY', 'JPY'), ('KRW', 'KRW'), ('KZT', 'KZT'), ('MXN', 'MXN'), ('MYR', 'MYR'), ('NOK', 'NOK'), ('NZD', 'NZD'), ('PAB', 'PAB'), ('PEN', 'PEN'), ('PHP', 'PHP'), ('PKR', 'PKR'), ('PLN', 'PLN'), ('PYG', 'PYG'), ('RON', 'RON'), ('RUB', 'RUB'), ('SAR', 'SAR'), ('SEK', 'SEK'), ('SAR', 'SAR'), ('SGD', 'SGD'), ('THB', 'THB'), ('TRY', 'TRY'), ('TWD', 'TWD'), ('UAH', 'UAH'), ('USD', 'USD'), ('UYU', 'UYU'), ('VND', 'VND'), ('ZAR', 'ZAR')], max_length=5, null=True)),
                ('our_rate', models.DecimalField(decimal_places=2, max_digits=15)),
                ('send_amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=20, null=True)),
                ('send_method', models.CharField(choices=[('bank', 'Bank Transfer'), ('cash', 'Cash Transfer'), ('cheque', 'Cheque Transfer')], max_length=30, null=True)),
                ('transfer_rate', models.DecimalField(decimal_places=2, max_digits=20, null=True)),
                ('receive_amount', models.DecimalField(decimal_places=2, max_digits=20, null=True)),
                ('account_name', models.CharField(max_length=100, null=True)),
                ('account_no', models.CharField(max_length=100, null=True)),
                ('branch_code', models.CharField(max_length=70, null=True)),
                ('bank_name', models.CharField(max_length=70, null=True)),
                ('bank_contact', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('bank_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('receive_method', models.CharField(choices=[('bank', 'Bank Transfer'), ('cash', 'Cash Transfer'), ('cheque', 'Cheque Transfer')], max_length=30, null=True)),
                ('transaction_id', models.CharField(default=customeraccess.models.generate_pk, editable=False, max_length=20)),
                ('money_status', models.CharField(blank=True, choices=[('Sent', 'Sent'), ('Ready To Collect', 'Ready To Collect'), ('Received', 'Received'), ('Cancelled', 'Cancelled')], default='Sent', max_length=30)),
                ('transaction_date', models.DateField(auto_now_add=True)),
                ('description', models.CharField(blank=True, max_length=150)),
                ('reason_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administration.reasontype')),
                ('receiver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='customeraccess.receiver')),
            ],
        ),
    ]
