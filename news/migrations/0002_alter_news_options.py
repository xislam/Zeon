# Generated by Django 4.0.4 on 2022-05-21 12:23
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="news",
            options={"verbose_name_plural": "News"},
        ),
    ]