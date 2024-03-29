# Generated by Django 4.0.4 on 2022-07-25 05:15
import django.db.models.deletion
from django.conf import settings
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Quiz",
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
                ("title", models.CharField(max_length=255, verbose_name="title")),
                (
                    "short_description",
                    models.TextField(verbose_name="short description"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="last updated at"),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="created at"),
                ),
            ],
            options={
                "verbose_name": "quiz",
                "verbose_name_plural": "quiz",
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="Topic",
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
                ("name", models.CharField(max_length=125, verbose_name="Name Topic")),
            ],
        ),
        migrations.CreateModel(
            name="Response",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "quiz",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tests",
                        to="quiz.quiz",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tests",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="quiz",
            name="topics",
            field=models.ManyToManyField(
                related_name="quizzes", to="quiz.topic", verbose_name="topics"
            ),
        ),
        migrations.CreateModel(
            name="Question",
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
                (
                    "type",
                    models.IntegerField(
                        choices=[
                            (0, "Text"),
                            (1, "Single Choice"),
                            (2, "Multiple Choice"),
                        ],
                        verbose_name="type",
                    ),
                ),
                ("title", models.CharField(max_length=2000, verbose_name="title")),
                ("time", models.TimeField(default="00:02:00")),
                (
                    "difficulty",
                    models.IntegerField(
                        choices=[(1, "easy"), (2, "medium"), (3, "hard")],
                        default=2,
                        verbose_name="difficulty",
                    ),
                ),
                (
                    "img",
                    models.ImageField(
                        blank=True, null=True, upload_to="q_img", verbose_name="image"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="last updated at"),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="created at"),
                ),
                (
                    "max_point",
                    models.PositiveSmallIntegerField(verbose_name="maximum point"),
                ),
                (
                    "is_active",
                    models.BooleanField(default=False, verbose_name="is active"),
                ),
                (
                    "quiz",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="questions",
                        to="quiz.quiz",
                    ),
                ),
            ],
            options={
                "verbose_name": "question",
                "verbose_name_plural": "questions",
            },
        ),
        migrations.CreateModel(
            name="Option",
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
                ("text", models.CharField(max_length=255, verbose_name="text")),
                (
                    "is_correct",
                    models.BooleanField(default=False, verbose_name="is correct"),
                ),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="options",
                        to="quiz.question",
                    ),
                ),
            ],
            options={
                "verbose_name": "option",
                "verbose_name_plural": "options",
            },
        ),
        migrations.CreateModel(
            name="Answer",
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
                ("text", models.TextField(blank=True, null=True, verbose_name="text")),
                ("point", models.PositiveSmallIntegerField(verbose_name="point")),
                ("options", models.ManyToManyField(to="quiz.option")),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="answers",
                        to="quiz.question",
                    ),
                ),
                (
                    "response",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="answers",
                        to="quiz.response",
                    ),
                ),
            ],
        ),
    ]
