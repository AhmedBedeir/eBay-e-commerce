# Generated by Django 4.0.6 on 2022-08-07 00:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0017_alter_listings_winner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bids',
            old_name='user',
            new_name='owner',
        ),
    ]
