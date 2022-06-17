# Generated by Django 4.0.4 on 2022-06-17 10:14
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("partner_site", "0006_alter_status_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="answer",
            options={
                "verbose_name": "Answer Partner",
                "verbose_name_plural": "Answer Partner",
            },
        ),
        migrations.AlterModelOptions(
            name="contactus",
            options={
                "verbose_name": "Contact Us Partner",
                "verbose_name_plural": "Contact Us Partner",
            },
        ),
        migrations.AlterModelOptions(
            name="cvstatus",
            options={
                "verbose_name": "CV Status Partner",
                "verbose_name_plural": "CV Status Partner",
            },
        ),
        migrations.AlterModelOptions(
            name="direction",
            options={
                "verbose_name": "Direction Partner",
                "verbose_name_plural": "Direction Partner",
            },
        ),
        migrations.AlterModelOptions(
            name="partnercv",
            options={"verbose_name": "Partner CV", "verbose_name_plural": "Partner CV"},
        ),
        migrations.AlterModelOptions(
            name="socialnetwork",
            options={
                "verbose_name": "Social Network Partner",
                "verbose_name_plural": "Social Network Partner",
            },
        ),
        migrations.AlterModelOptions(
            name="status",
            options={
                "verbose_name": "Contact Us Partner Status",
                "verbose_name_plural": "Contact Us Partner Status",
            },
        ),
    ]