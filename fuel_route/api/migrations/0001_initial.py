# Generated by Django 3.2.23 on 2025-01-28 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FuelPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('truckstop_name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('state', models.CharField(max_length=2)),
                ('retail_price', models.FloatField()),
            ],
        ),
    ]
