# Generated by Django 3.1.7 on 2021-03-14 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donationapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentGatewaySettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_id', models.CharField(blank=True, max_length=500, null=True)),
                ('store_pass', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'verbose_name': 'PaymentGatewaySetting',
                'verbose_name_plural': 'PaymentGatewaySettings',
                'db_table': 'paymentgatewaysettings',
            },
        ),
    ]
