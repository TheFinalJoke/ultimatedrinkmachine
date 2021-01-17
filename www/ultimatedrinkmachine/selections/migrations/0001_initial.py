# Generated by Django 3.1.5 on 2021-01-17 03:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PumpToALiquid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liquid', models.CharField(max_length=200)),
                ('pump_num', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(9)])),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('alcohol', models.CharField(max_length=200)),
                ('mixer', models.CharField(max_length=200)),
            ],
        ),
    ]
