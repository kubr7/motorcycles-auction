# Generated by Django 5.0.2 on 2024-07-12 22:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0128_alter_motorcycle_end_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motorcycle',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 12, 22, 44, 22, 286247, tzinfo=datetime.timezone.utc)),
        ),
    ]