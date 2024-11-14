# Generated by Django 4.2.5 on 2023-12-28 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0006_rename_title_listing_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='isExpired',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='listing',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
