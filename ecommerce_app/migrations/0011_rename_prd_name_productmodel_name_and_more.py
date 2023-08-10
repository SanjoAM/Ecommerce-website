# Generated by Django 4.2.3 on 2023-08-06 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ecommerce_app", "0010_alter_cartmodel_quantity_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="productmodel",
            old_name="prd_name",
            new_name="name",
        ),
        migrations.RenameField(
            model_name="productmodel",
            old_name="prd_price",
            new_name="price",
        ),
        migrations.RemoveField(
            model_name="productmodel",
            name="prd_image",
        ),
        migrations.AddField(
            model_name="productmodel",
            name="image",
            field=models.ImageField(null=True, upload_to="products/"),
        ),
    ]