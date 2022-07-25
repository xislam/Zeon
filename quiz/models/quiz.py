from django.db import models
from django.utils.translation import gettext_lazy as _

from root import settings


class Weight(models.IntegerChoices):
    EASY = 1, _("easy")
    MEDIUM = 2, _("medium")
    HARD = 3, _("hard")


class Type(models.TextChoices):
    TEXT = "text", _("text")
    SELECT = "select", _("select")
    MULTIPLE = "multiple", _("multiple choice")


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Topic(models.Model):
    name = models.CharField(max_length=125, verbose_name=_("Name Topic"))

    def __str__(self):
        return self.name


class Quiz(models.Model):
    title = models.CharField(_("title"), max_length=255)
    topics = models.ManyToManyField(
        Topic, related_name="quizzes", verbose_name=_("topics")
    )
    short_description = models.TextField(_("short description"))
    updated_at = models.DateTimeField(_("last updated at"), auto_now=True)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)

    class Meta:
        verbose_name = _("quiz")
        verbose_name_plural = _("quiz")
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class Question(models.Model):
    TYPE = (
        (0, _("Text")),
        (1, _("Single Choice")),
        (2, _("Multiple Choice")),
    )

    quiz = models.ForeignKey("Quiz", models.CASCADE, "questions")
    type = models.IntegerField(_("type"), choices=TYPE)
    title = models.CharField(_("title"), max_length=2000)
    time = models.TimeField(default="00:02:00")
    difficulty = models.IntegerField(
        _("difficulty"), choices=Weight.choices, default=Weight.MEDIUM
    )
    img = models.ImageField(_("image"), upload_to="q_img", null=True, blank=True)
    updated_at = models.DateTimeField(_("last updated at"), auto_now=True)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    max_point = models.PositiveSmallIntegerField(_("maximum point"))
    is_active = models.BooleanField(_("is active"), default=False)

    class Meta:
        verbose_name = _("question")
        verbose_name_plural = _("questions")

    def __str__(self):
        return self.title


class Option(models.Model):
    question = models.ForeignKey("Question", models.CASCADE, "options")
    text = models.CharField(_("text"), max_length=255)
    is_correct = models.BooleanField(_("is correct"), default=False)

    class Meta:
        verbose_name = _("option")
        verbose_name_plural = _("options")

    def __str__(self):
        return self.text


class Response(models.Model):
    quiz = models.ForeignKey("Quiz", models.CASCADE, "tests")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE, "tests")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        pass


class Answer(models.Model):
    response = models.ForeignKey("Response", models.CASCADE, "answers")
    question = models.ForeignKey("Question", models.CASCADE, "answers")
    text = models.TextField(_("text"), null=True, blank=True)
    options = models.ManyToManyField("Option")
    point = models.PositiveSmallIntegerField(_("point"))
