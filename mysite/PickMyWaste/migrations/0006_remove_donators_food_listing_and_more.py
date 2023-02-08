# Generated by Django 4.1.5 on 2023-02-03 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("PickMyWaste", "0005_alter_food_donator"),
    ]

    operations = [
        migrations.RemoveField(model_name="donators", name="food_listing",),
        migrations.RemoveField(model_name="donators", name="food_quantity",),
        migrations.AddField(
            model_name="donators",
            name="address",
            field=models.CharField(default="", max_length=300),
        ),
        migrations.AddField(
            model_name="donators",
            name="phone",
            field=models.CharField(default="", max_length=100),
        ),
    ]
