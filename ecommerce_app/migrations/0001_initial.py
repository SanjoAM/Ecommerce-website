# Generated by Django 4.2.3 on 2023-08-02 05:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CategoryModel",
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
                ("cat_name", models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name="CustomerModel",
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
                ("cus_name", models.CharField(max_length=70)),
                ("cus_password", models.CharField(max_length=70)),
                ("cus_address", models.CharField(max_length=70)),
                ("cus_phone", models.CharField(max_length=70)),
                ("cus_image", models.ImageField(null=True, upload_to="image/")),
            ],
        ),
        migrations.CreateModel(
            name="ProductModel",
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
                ("prd_name", models.CharField(max_length=70)),
                ("prd_description", models.CharField(max_length=70)),
                ("prd_image", models.ImageField(null=True, upload_to="iamge/")),
                ("prd_addate", models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="CartModel",
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
                ("quantity", models.PositiveIntegerField(default=1)),
                ("added_at", models.DateTimeField(auto_now_add=True)),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ecommerce_app.customermodel",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ecommerce_app.productmodel",
                    ),
                ),
            ],
        ),
    ]