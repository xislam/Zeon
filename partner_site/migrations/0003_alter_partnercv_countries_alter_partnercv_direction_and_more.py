# Generated by Django 4.0.4 on 2022-06-17 08:37
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("partner_site", "0002_delete_cv"),
    ]

    operations = [
        migrations.AlterField(
            model_name="partnercv",
            name="countries",
            field=models.CharField(max_length=225, verbose_name="Countries"),
        ),
        migrations.AlterField(
            model_name="partnercv",
            name="direction",
            field=models.CharField(max_length=125, verbose_name="Direction"),
        ),
        migrations.AlterField(
            model_name="partnercv",
            name="file_cv",
            field=models.FileField(
                upload_to="File_cv_p", verbose_name="File PartnerCV"
            ),
        ),
        migrations.AlterField(
            model_name="partnercv",
            name="question",
            field=models.CharField(max_length=300, verbose_name="Question"),
        ),
    ]
