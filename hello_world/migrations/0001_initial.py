# Generated by Django 2.1 on 2018-08-17 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Iata',
            fields=[
                ('iata_code', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('lat', models.DecimalField(decimal_places=7, max_digits=15)),
                ('lng', models.DecimalField(decimal_places=7, max_digits=15)),
            ],
        ),
    ]
