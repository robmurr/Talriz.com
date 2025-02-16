# Generated by Django 5.1.3 on 2024-12-05 03:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("talriz_app", "0007_auto_20241124_2002"),
    ]

    operations = [
        migrations.CreateModel(
            name="Message",
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
                ("buyer", models.TextField()),
                ("seller", models.TextField()),
                ("data", models.TextField()),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
