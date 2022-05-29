# Generated by Django 4.0.4 on 2022-05-29 13:54
import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("career", "0005_alter_career_country"),
    ]

    operations = [
        migrations.AlterField(
            model_name="career",
            name="country",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="country",
                to="career.country",
                verbose_name="Country",
            ),
        ),
    ]
