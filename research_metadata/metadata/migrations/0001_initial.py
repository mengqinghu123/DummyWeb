# Generated by Django 5.0.6 on 2024-07-10 16:14

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ResearchMetadata",
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
                ("data_provider", models.CharField(max_length=100)),
                ("data_format", models.CharField(max_length=100)),
                ("degree_of_aggregation", models.CharField(max_length=100)),
            ],
        ),
    ]
