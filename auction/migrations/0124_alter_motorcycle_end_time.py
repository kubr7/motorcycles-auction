# Generated by Django 5.0.2 on 2024-07-12 22:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0123_enginecapacity_alter_motorcycle_end_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motorcycle',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 12, 22, 10, 18, 195749, tzinfo=datetime.timezone.utc)),
        ),
    ]
