# Generated by Django 5.0.2 on 2024-07-02 23:19

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0050_alter_listing_end_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_user_pic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='commentUserPic', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='listing',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 3, 23, 19, 34, 500367, tzinfo=datetime.timezone.utc)),
        ),
    ]
