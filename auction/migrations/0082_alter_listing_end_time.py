# Generated by Django 5.0.2 on 2024-07-08 23:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0081_remove_listing_bid_price_bid_listing_bid_timestamp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 9, 0, 25, 45, 372881, tzinfo=datetime.timezone.utc)),
        ),
    ]