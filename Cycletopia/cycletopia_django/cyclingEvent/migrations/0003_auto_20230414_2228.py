# Generated by Django 3.1.7 on 2023-04-14 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cyclingEvent', '0002_event_date_and_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='map_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
