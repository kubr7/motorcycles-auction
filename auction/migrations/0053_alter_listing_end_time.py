# Generated by Django 5.0.2 on 2024-07-02 23:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0052_remove_comment_comment_user_pic_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 3, 23, 29, 38, 220714, tzinfo=datetime.timezone.utc)),
        ),
    ]
