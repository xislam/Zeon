# Generated by Django 4.0.4 on 2022-06-18 19:41
import datetime

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("quiz", "0006_question_img"),
    ]

    operations = [
        migrations.AddField(
            model_name="quizzes",
            name="time",
            field=models.TimeField(default=datetime.time),
            preserve_default=False,
        ),
    ]