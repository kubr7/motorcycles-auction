# Generated by Django 5.1.3 on 2024-11-14 17:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0146_alter_motorcycle_end_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motorcycle',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 14, 18, 3, 6, 217558, tzinfo=datetime.timezone.utc)),
        ),
    ]
