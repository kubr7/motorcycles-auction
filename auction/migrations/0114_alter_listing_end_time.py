# Generated by Django 5.0.2 on 2024-07-10 19:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0113_alter_listing_end_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 10, 20, 1, 41, 53161, tzinfo=datetime.timezone.utc)),
        ),
    ]