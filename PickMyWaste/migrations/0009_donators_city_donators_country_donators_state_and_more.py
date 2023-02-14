# Generated by Django 4.1.5 on 2023-02-14 03:41

import address.models
from django.db import migrations, models
import django.db.models.deletion
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ("address", "0003_auto_20200830_1851"),
        ("PickMyWaste", "0008_donators_latitude_donators_longitude_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="donators",
            name="city",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="donators",
            name="country",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="donators",
            name="state",
            field=localflavor.us.models.USStateField(
                blank=True, max_length=2, null=True
            ),
        ),
        migrations.AddField(
            model_name="donators",
            name="zipcode",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="donators",
            name="address",
            field=address.models.AddressField(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                to="address.address",
            ),
        ),
    ]