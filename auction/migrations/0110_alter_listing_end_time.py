# Generated by Django 5.0.2 on 2024-07-10 06:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0109_alter_listing_end_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 10, 6, 45, 30, 223305, tzinfo=datetime.timezone.utc)),
        ),
    ]
