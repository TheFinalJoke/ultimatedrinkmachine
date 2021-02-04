# Generated by Django 3.1.5 on 2021-01-20 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selections', '0003_auto_20210117_2231'),
    ]

    operations = [
        migrations.AddField(
            model_name='pumptoaliquid',
            name='liquid_type',
            field=models.CharField(choices=[(1, 'Alcohol'), (2, 'Mixer')], default='Alcohol', max_length=50),
        ),
        migrations.AlterField(
            model_name='pumptoaliquid',
            name='pump_num',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
