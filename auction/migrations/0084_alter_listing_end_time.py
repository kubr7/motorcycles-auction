# Generated by Django 5.0.2 on 2024-07-08 23:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0083_alter_listing_end_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 9, 0, 38, 55, 786521, tzinfo=datetime.timezone.utc)),
        ),
    ]