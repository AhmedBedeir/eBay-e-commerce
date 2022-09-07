# Generated by Django 4.0.6 on 2022-08-07 15:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0020_alter_listings_winner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bids',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bidsUser', to=settings.AUTH_USER_MODEL),
        ),
    ]