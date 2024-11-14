# Generated by Django 5.0.2 on 2024-07-02 05:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0041_alter_listing_cylinders_alter_listing_end_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='displacement',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='listing',
            name='power',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='listing',
            name='torque',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='listing',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 3, 5, 7, 30, 239562, tzinfo=datetime.timezone.utc)),
        ),
    ]