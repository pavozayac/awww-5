# Generated by Django 5.0.4 on 2024-04-16 09:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Picture",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                (
                    "height",
                    models.PositiveIntegerField(verbose_name="Height of the picture"),
                ),
                (
                    "width",
                    models.PositiveIntegerField(verbose_name="Width of the picture"),
                ),
                ("editors", models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name="Rectangle",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                (
                    "x",
                    models.PositiveIntegerField(
                        verbose_name="Position in the X coordinate"
                    ),
                ),
                (
                    "y",
                    models.PositiveIntegerField(
                        verbose_name="Position in the Y coordinate"
                    ),
                ),
                (
                    "height",
                    models.PositiveIntegerField(verbose_name="Height of the rectangle"),
                ),
                (
                    "width",
                    models.PositiveIntegerField(verbose_name="Width of the rectangle"),
                ),
                (
                    "fill",
                    models.CharField(
                        max_length=30, verbose_name="Fill color of the rectangle"
                    ),
                ),
                (
                    "picture",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="rectangles",
                        to="cms.picture",
                    ),
                ),
            ],
        ),
    ]