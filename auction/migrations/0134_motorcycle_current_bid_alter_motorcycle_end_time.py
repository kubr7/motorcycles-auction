# Generated by Django 5.0.2 on 2024-07-13 01:46

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0133_alter_motorcycle_end_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='motorcycle',
            name='current_bid',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='current_bid', to='auction.bid'),
        ),
        migrations.AlterField(
            model_name='motorcycle',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 13, 1, 56, 22, 702345, tzinfo=datetime.timezone.utc)),
        ),
    ]