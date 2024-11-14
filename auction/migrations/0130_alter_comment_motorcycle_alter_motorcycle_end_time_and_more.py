# Generated by Django 5.0.2 on 2024-07-12 22:36

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0129_alter_motorcycle_end_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='motorcycle',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='motorcycleComment', to='auction.motorcycle'),
        ),
        migrations.AlterField(
            model_name='motorcycle',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 12, 22, 46, 27, 673379, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='motorcycle',
            name='watchlist',
            field=models.ManyToManyField(blank=True, related_name='motorcycleWatchList', to=settings.AUTH_USER_MODEL),
        ),
    ]
