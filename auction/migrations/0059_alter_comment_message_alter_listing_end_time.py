# Generated by Django 5.0.2 on 2024-07-07 20:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0058_alter_comment_author_alter_comment_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='message',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='listing',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 9, 20, 1, 26, 284489, tzinfo=datetime.timezone.utc)),
        ),
    ]