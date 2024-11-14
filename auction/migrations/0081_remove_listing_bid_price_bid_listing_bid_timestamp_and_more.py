# Generated by Django 5.0.2 on 2024-07-08 23:21

import datetime
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0080_remove_bid_listing_remove_bid_timestamp_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='bid_price',
        ),
        migrations.AddField(
            model_name='bid',
            name='listing',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auction.listing'),
        ),
        migrations.AddField(
            model_name='bid',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='listing',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 9, 0, 21, 50, 334160, tzinfo=datetime.timezone.utc)),
        ),
    ]
