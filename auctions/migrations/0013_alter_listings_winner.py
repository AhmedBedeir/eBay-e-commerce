# Generated by Django 4.0.6 on 2022-08-04 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_listings_watchlist_listings_winner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='winner',
            field=models.CharField(default='', max_length=100, null=True),
        ),
    ]
