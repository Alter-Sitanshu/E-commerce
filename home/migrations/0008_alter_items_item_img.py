# Generated by Django 5.1.3 on 2024-12-01 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0007_alter_cart_items"),
    ]

    operations = [
        migrations.AlterField(
            model_name="items",
            name="item_img",
            field=models.ImageField(default="default.png", upload_to="item_images"),
        ),
    ]
