# Generated by Django 5.0.2 on 2024-07-12 22:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0125_alter_motorcycle_engine_capacity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motorcycle',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 12, 22, 21, 26, 348200, tzinfo=datetime.timezone.utc)),
        ),
    ]
