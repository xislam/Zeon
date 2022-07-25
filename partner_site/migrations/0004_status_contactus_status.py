# Generated by Django 4.0.4 on 2022-06-17 09:44
import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        (
            "partner_site",
            "0003_alter_partnercv_countries_alter_partnercv_direction_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="Status",
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
                    "status_name",
                    models.CharField(max_length=125, verbose_name="Status name"),
                ),
            ],
        ),
        migrations.AddField(
            model_name="contactus",
            name="status",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="partner_site.status",
                verbose_name="Status",
            ),
        ),
    ]
