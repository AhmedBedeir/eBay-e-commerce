# Generated by Django 4.0.6 on 2022-08-04 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0014_alter_listings_startingbid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='category',
            field=models.CharField(choices=[('fashion', 'Fashion'), ('toys', 'Toys'), ('electronics', 'Electronics'), ('watches', 'Watches'), ('other', 'Other')], max_length=50),
        ),
    ]
