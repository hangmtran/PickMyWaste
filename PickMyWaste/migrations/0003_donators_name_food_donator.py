# Generated by Django 4.1.5 on 2023-02-03 06:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        (
            "PickMyWaste",
            "0002_remove_donators_pub_date_alter_food_description_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="donators",
            name="name",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AddField(
            model_name="food",
            name="donator",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                to="PickMyWaste.donators",
            ),
        ),
    ]
