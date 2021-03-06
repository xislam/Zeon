# Generated by Django 4.0.4 on 2022-05-29 21:50
import ckeditor.fields
import django.db.models.deletion
import phonenumber_field.modelfields
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Career",
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
                ("name", models.CharField(max_length=125, verbose_name="Vacancy name")),
                (
                    "short_description",
                    models.TextField(verbose_name="Short description"),
                ),
                (
                    "description",
                    ckeditor.fields.RichTextField(verbose_name="Description"),
                ),
                ("remote", models.BooleanField(default=False, verbose_name="Remote")),
                ("office", models.BooleanField(default=False, verbose_name="Office")),
                (
                    "relocation",
                    models.BooleanField(default=False, verbose_name="Relocation"),
                ),
                (
                    "date_create",
                    models.DateTimeField(auto_now_add=True, verbose_name="Date create"),
                ),
                (
                    "archived",
                    models.BooleanField(default=False, verbose_name="Archived"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Country",
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
                ("name", models.CharField(max_length=125, verbose_name="Country")),
                (
                    "flag",
                    models.ImageField(upload_to="location", verbose_name="Photo flag"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Direction",
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
                ("name", models.CharField(max_length=125, verbose_name="Name")),
                (
                    "date_create",
                    models.DateTimeField(auto_now_add=True, verbose_name="Date create"),
                ),
            ],
        ),
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
                ("name", models.CharField(max_length=125, verbose_name="Status")),
            ],
        ),
        migrations.CreateModel(
            name="PartnerCV",
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
                ("name", models.CharField(max_length=125, verbose_name="Name")),
                ("surname", models.CharField(max_length=125, verbose_name="Surname")),
                (
                    "phone_number",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, region=None, verbose_name="Phone number"
                    ),
                ),
                ("email", models.EmailField(max_length=254, verbose_name="Email")),
                (
                    "cv_file",
                    models.FileField(
                        upload_to="CV_file", verbose_name="Summary PartnerCV"
                    ),
                ),
                (
                    "date_create",
                    models.DateTimeField(
                        auto_now_add=True, null=True, verbose_name="Date"
                    ),
                ),
                (
                    "career",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="career.career",
                        verbose_name="Vacancy",
                    ),
                ),
                (
                    "status",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="career.status",
                        verbose_name="Status",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="career",
            name="country",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="country",
                to="career.country",
                verbose_name="Country",
            ),
        ),
        migrations.AddField(
            model_name="career",
            name="direction",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="career.direction",
                verbose_name="Direction",
            ),
        ),
    ]
