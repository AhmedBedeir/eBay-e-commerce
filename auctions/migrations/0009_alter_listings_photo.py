# Generated by Django 4.0.6 on 2022-08-03 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_alter_listings_createdon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='photo',
            field=models.ImageField(blank=True, default='./images/default.png', null=True, upload_to='listing'),
        ),
    ]
