# Generated by Django 5.0.2 on 2024-07-08 20:45

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0070_remove_listing_collections_alter_listing_end_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='collections',
            field=models.ManyToManyField(blank=True, related_name='listingCollections', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='listing',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 8, 21, 45, 47, 547804, tzinfo=datetime.timezone.utc)),
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]