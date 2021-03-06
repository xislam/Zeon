# Generated by Django 4.0.4 on 2022-07-12 11:39
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("quiz", "0003_question_img_user_otp"),
    ]

    operations = [
        migrations.AlterField(
            model_name="answer",
            name="is_correct",
            field=models.BooleanField(default=False, verbose_name="is correct"),
        ),
        migrations.AlterField(
            model_name="answer",
            name="label",
            field=models.CharField(max_length=100, verbose_name="Label"),
        ),
        migrations.AlterField(
            model_name="answer",
            name="question",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="quiz.question",
                verbose_name="Question",
            ),
        ),
        migrations.AlterField(
            model_name="question",
            name="label",
            field=models.CharField(max_length=300, verbose_name="Label"),
        ),
        migrations.AlterField(
            model_name="question",
            name="order",
            field=models.IntegerField(default=0, verbose_name="Order"),
        ),
        migrations.AlterField(
            model_name="question",
            name="quiz",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="quiz.quiz",
                verbose_name="Quiz",
            ),
        ),
        migrations.AlterField(
            model_name="quiz",
            name="description",
            field=models.CharField(max_length=300, verbose_name="Descriptions"),
        ),
        migrations.AlterField(
            model_name="quiz",
            name="image",
            field=models.ImageField(upload_to="Quiz_img", verbose_name="Image"),
        ),
        migrations.AlterField(
            model_name="quiz",
            name="name",
            field=models.CharField(max_length=300, verbose_name="Name"),
        ),
        migrations.AlterField(
            model_name="quiz",
            name="roll_out",
            field=models.BooleanField(default=False, verbose_name="Roll out"),
        ),
        migrations.AlterField(
            model_name="quiz",
            name="slug",
            field=models.SlugField(blank=True, verbose_name="Slug"),
        ),
        migrations.AlterField(
            model_name="quiz",
            name="timestamp",
            field=models.DateTimeField(auto_now_add=True, verbose_name="Time stamp"),
        ),
        migrations.AlterField(
            model_name="quiztaker",
            name="completed",
            field=models.BooleanField(default=False, verbose_name="Completed"),
        ),
        migrations.AlterField(
            model_name="quiztaker",
            name="date_completed",
            field=models.DateTimeField(
                default=None, null=True, verbose_name="Date_completed"
            ),
        ),
        migrations.AlterField(
            model_name="quiztaker",
            name="quiz",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="quiz.quiz",
                verbose_name="Quiz",
            ),
        ),
        migrations.AlterField(
            model_name="quiztaker",
            name="score",
            field=models.IntegerField(default=0, verbose_name="Score"),
        ),
        migrations.AlterField(
            model_name="quiztaker",
            name="timestamp",
            field=models.DateTimeField(auto_now_add=True, verbose_name="Time stamp"),
        ),
        migrations.AlterField(
            model_name="quiztaker",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="User",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="created_at",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="Create at"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(max_length=254, unique=True, verbose_name="Email"),
        ),
        migrations.AlterField(
            model_name="user",
            name="is_active",
            field=models.BooleanField(default=True, verbose_name="Is active"),
        ),
        migrations.AlterField(
            model_name="user",
            name="is_staff",
            field=models.BooleanField(default=False, verbose_name="Is staff"),
        ),
        migrations.AlterField(
            model_name="user",
            name="is_superadmin",
            field=models.BooleanField(default=False, verbose_name="Is super admin"),
        ),
        migrations.AlterField(
            model_name="user",
            name="name",
            field=models.CharField(max_length=100, verbose_name="Name"),
        ),
        migrations.AlterField(
            model_name="user",
            name="otp",
            field=models.CharField(
                blank=True, max_length=6, null=True, verbose_name="OTP"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="password",
            field=models.CharField(max_length=255, verbose_name="Password"),
        ),
        migrations.AlterField(
            model_name="user",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, verbose_name="Updated at"),
        ),
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(
                max_length=100, unique=True, verbose_name="Username"
            ),
        ),
        migrations.AlterField(
            model_name="usersanswer",
            name="answer",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="quiz.answer",
                verbose_name="Answer",
            ),
        ),
        migrations.AlterField(
            model_name="usersanswer",
            name="question",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="quiz.question",
                verbose_name="Question",
            ),
        ),
        migrations.AlterField(
            model_name="usersanswer",
            name="quiz_taker",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="quiz.quiztaker",
                verbose_name="Quiz taker",
            ),
        ),
    ]
