# Generated by Django 5.0.2 on 2024-07-07 01:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0055_comment_created_at_comment_parent_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 8, 1, 11, 42, 252510, tzinfo=datetime.timezone.utc)),
        ),
    ]
