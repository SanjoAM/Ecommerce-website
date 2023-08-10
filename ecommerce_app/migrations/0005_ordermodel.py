# Generated by Django 4.2.3 on 2023-08-03 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("ecommerce_app", "0004_productmodel_prd_price_alter_productmodel_prd_addate"),
    ]

    operations = [
        migrations.CreateModel(
            name="OrderModel",
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
                ("order_number", models.CharField(max_length=20, unique=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("total_amount", models.DecimalField(decimal_places=2, max_digits=10)),
                ("order_status", models.CharField(default="Processing", max_length=20)),
                ("shipping_address", models.CharField(max_length=200)),
                ("contact_number", models.CharField(max_length=15)),
                ("payment_method", models.CharField(max_length=50)),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ecommerce_app.customermodel",
                    ),
                ),
            ],
        ),
    ]
