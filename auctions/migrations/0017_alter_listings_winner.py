# Generated by Django 4.0.6 on 2022-08-06 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0016_bids'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='winner',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
