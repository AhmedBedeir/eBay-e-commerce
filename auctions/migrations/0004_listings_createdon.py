# Generated by Django 4.0.6 on 2022-08-02 15:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_alter_listings_owner_alter_listings_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='listings',
            name='createdOn',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
