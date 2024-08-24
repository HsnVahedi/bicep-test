# Generated by Django 3.1.7 on 2021-03-30 22:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("relecloud", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Destination",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, unique=True)),
                ("description", models.TextField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name="InfoRequest",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, unique=True)),
                ("email", models.EmailField(max_length=254)),
                ("notes", models.TextField(max_length=2000)),
            ],
        ),
        migrations.RemoveField(
            model_name="cruisecabin",
            name="cabin",
        ),
        migrations.RemoveField(
            model_name="cruisecabin",
            name="cruise",
        ),
        migrations.RenameField(
            model_name="cruise",
            old_name="destination",
            new_name="name",
        ),
        migrations.DeleteModel(
            name="Cabin",
        ),
        migrations.DeleteModel(
            name="CruiseCabin",
        ),
        migrations.AddField(
            model_name="inforequest",
            name="cruise",
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to="relecloud.cruise"),
        ),
        migrations.AddField(
            model_name="cruise",
            name="destinations",
            field=models.ManyToManyField(to="relecloud.Destination"),
        ),
    ]
