# Generated by Django 5.0.2 on 2024-07-08 20:03

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0068_alter_listing_end_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='collections',
            field=models.ManyToManyField(blank=True, related_name='in_collections', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='listing',
            name='bid_price',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bidPrice', to='auction.bid'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 8, 21, 3, 0, 958091, tzinfo=datetime.timezone.utc)),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collections', models.ManyToManyField(blank=True, related_name='in_collections', to='auction.listing')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]