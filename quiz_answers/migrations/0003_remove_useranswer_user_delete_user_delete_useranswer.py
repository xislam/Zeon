# Generated by Django 4.0.4 on 2022-07-03 12:14
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("quiz_answers", "0002_alter_user_create_date"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="useranswer",
            name="user",
        ),
        migrations.DeleteModel(
            name="User",
        ),
        migrations.DeleteModel(
            name="UserAnswer",
        ),
    ]
