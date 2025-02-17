# Generated by Django 5.1.3 on 2024-11-29 15:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_alter_items_seller"),
        ("login", "0002_delete_usermodel"),
    ]

    operations = [
        migrations.AlterField(
            model_name="items",
            name="date_added",
            field=models.DateField(auto_now_add=True),
        ),
        migrations.CreateModel(
            name="Cart",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "account",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cart",
                        to="login.account",
                    ),
                ),
                ("items", models.ManyToManyField(related_name="cart", to="home.items")),
            ],
        ),
    ]
