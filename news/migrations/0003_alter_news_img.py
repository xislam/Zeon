# Generated by Django 4.0.4 on 2022-05-29 16:59
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0002_alter_news_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="news",
            name="img",
            field=models.ImageField(upload_to="news", verbose_name="Photo for news"),
        ),
    ]