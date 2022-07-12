from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _

from .manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(_("Name"), max_length=100)
    email = models.EmailField(_("Email"), unique=True)
    username = models.CharField(_("Username"), max_length=100, unique=True)
    password = models.CharField(_("Password"), max_length=255)
    is_staff = models.BooleanField(_("Is staff"), default=False)
    is_superadmin = models.BooleanField(_("Is super admin"), default=False)
    otp = models.CharField(_("OTP"), max_length=6, null=True, blank=True)
    is_active = models.BooleanField(_("Is active"), default=True)
    created_at = models.DateTimeField(_("Create at"), default=timezone.now)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)
    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "username"]

    def __str__(self):
        return self.email


class Quiz(models.Model):
    name = models.CharField(_("Name"), max_length=300)
    description = models.CharField(_("Descriptions"), max_length=300)
    image = models.ImageField(_("Image"), upload_to="Quiz_img")
    slug = models.SlugField(_("Slug"), max_length=50, blank=True)
    roll_out = models.BooleanField(_("Roll out"), default=False)
    timestamp = models.DateTimeField(_("Time stamp"), auto_now_add=True)

    class Meta:
        ordering = [
            "timestamp",
        ]
        verbose_name_plural = "Quizzes"

    def __str__(self):
        return self.name


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, verbose_name=_("Quiz"), on_delete=models.CASCADE)
    label = models.CharField(_("Label"), max_length=300)
    img = models.ImageField(verbose_name="question_img", upload_to="question_img")
    order = models.IntegerField(_("Order"), default=0)

    def __str__(self):
        return self.label


class Answer(models.Model):
    question = models.ForeignKey(
        Question, verbose_name=_("Question"), on_delete=models.CASCADE
    )
    label = models.CharField(_("Label"), max_length=100)
    is_correct = models.BooleanField(_("is correct"), default=False)

    def __str__(self):
        return self.label


class QuizTaker(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name=_("User"), on_delete=models.CASCADE
    )
    quiz = models.ForeignKey(Quiz, verbose_name=_("Quiz"), on_delete=models.CASCADE)
    score = models.IntegerField(_("Score"), default=0)
    completed = models.BooleanField(_("Completed"), default=False)
    timestamp = models.DateTimeField(_("Time stamp"), auto_now_add=True)
    date_completed = models.DateTimeField(_("Date_completed"), default=None, null=True)

    def __str__(self):
        return self.user.email


class UsersAnswer(models.Model):
    quiz_taker = models.ForeignKey(
        QuizTaker, verbose_name=_("Quiz taker"), on_delete=models.CASCADE
    )
    question = models.ForeignKey(
        Question, verbose_name=_("Question"), on_delete=models.CASCADE
    )
    answer = models.ForeignKey(
        Answer, verbose_name=_("Answer"), on_delete=models.CASCADE, null=True
    )

    def __str__(self):
        return self.question.label
