# Generated by Django 5.0.2 on 2024-07-09 01:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0089_alter_listing_current_bid_alter_listing_end_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 9, 2, 8, 32, 55188, tzinfo=datetime.timezone.utc)),
        ),
    ]
