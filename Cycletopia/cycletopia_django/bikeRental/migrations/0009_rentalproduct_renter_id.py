# Generated by Django 3.1.7 on 2023-02-21 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bikeRental', '0008_rentalproduct_renter_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentalproduct',
            name='renter_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
