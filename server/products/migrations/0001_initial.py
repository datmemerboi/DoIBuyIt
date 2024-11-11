# Generated by Django 5.1.2 on 2024-11-11 13:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('barcode', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('brand', models.CharField(max_length=255)),
                ('image', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('name', models.CharField(choices=[('WWL', 'WWL')], max_length=5, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='VendorProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.vendor')),
            ],
            options={
                'unique_together': {('product', 'vendor')},
            },
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('viewed_date', models.DateTimeField()),
                ('tentative_end_date', models.DateTimeField()),
                ('cost_per_unit', models.FloatField(default=-1)),
                ('cost_per_unit_measure', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prices', to='products.product')),
                ('vendor_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prices', to='products.vendorproduct')),
            ],
        ),
    ]
