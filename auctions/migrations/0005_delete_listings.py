# Generated by Django 4.0.6 on 2022-08-02 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_listings_createdon'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Listings',
        ),
    ]