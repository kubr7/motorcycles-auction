# Generated by Django 5.0.2 on 2024-07-02 02:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0038_listing_cylinders_alter_listing_end_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='cylinders',
            field=models.IntegerField(default=4),
        ),
        migrations.AlterField(
            model_name='listing',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 3, 2, 51, 14, 102221, tzinfo=datetime.timezone.utc)),
        ),
    ]