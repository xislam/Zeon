# Generated by Django 4.0.4 on 2022-05-28 10:43
import ckeditor.fields
import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("career", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="career",
            name="office",
            field=models.BooleanField(default=False, verbose_name="Office"),
        ),
        migrations.AddField(
            model_name="career",
            name="relocation",
            field=models.BooleanField(default=False, verbose_name="Relocation"),
        ),
        migrations.AddField(
            model_name="career",
            name="text",
            field=ckeditor.fields.RichTextField(default=34, verbose_name="Description"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="career",
            name="country",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="career.country",
                verbose_name="Country",
            ),
        ),
        migrations.AlterField(
            model_name="career",
            name="remote",
            field=models.BooleanField(default=False, verbose_name="Remote"),
        ),
    ]