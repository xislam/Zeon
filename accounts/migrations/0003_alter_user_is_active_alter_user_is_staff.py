# Generated by Django 4.0.4 on 2022-07-25 05:31
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_user_otp_alter_user_id_alter_user_is_active"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="is_staff",
            field=models.BooleanField(default=True),
        ),
    ]