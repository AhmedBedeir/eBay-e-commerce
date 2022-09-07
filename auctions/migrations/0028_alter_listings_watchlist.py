# Generated by Django 4.0.6 on 2022-08-08 12:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0027_alter_comment_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='watchList',
            field=models.ManyToManyField(blank=True, related_name='watchList', to=settings.AUTH_USER_MODEL),
        ),
    ]