# Generated by Django 3.1.7 on 2023-02-21 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bikeRental', '0009_rentalproduct_renter_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentalproduct',
            name='stripe_token',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
