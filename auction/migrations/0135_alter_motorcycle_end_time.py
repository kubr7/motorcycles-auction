# Generated by Django 5.0.2 on 2024-07-13 02:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0134_motorcycle_current_bid_alter_motorcycle_end_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motorcycle',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 13, 2, 12, 28, 904127, tzinfo=datetime.timezone.utc)),
        ),
    ]