# Generated by Django 3.2 on 2022-02-28 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billmanage', '0002_auto_20210627_0417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='hsncode',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
