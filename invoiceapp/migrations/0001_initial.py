# Generated by Django 3.2 on 2022-02-27 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=255)),
                ('product_name', models.TextField()),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.IntegerField()),
                ('sub_total', models.IntegerField()),
                ('Payment_method', models.TextField(blank=True, null=True)),
                ('Shipping_charge', models.IntegerField()),
                ('total', models.IntegerField()),
                ('notes', models.TextField(blank=True, null=True)),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoiceapp.product')),
            ],
        ),
    ]
