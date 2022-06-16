from django.db import models
from django.utils.translation import gettext as _
from phonenumber_field.modelfields import PhoneNumberField


class SocialNetwork(models.Model):
    name = models.CharField(max_length=125, verbose_name=_("Name"))

    def __str__(self):
        return self.name


class ContactUs(models.Model):
    name = models.CharField(max_length=125, verbose_name=_("Name"))
    email = models.EmailField(verbose_name=_("Email"))
    social_network = models.ForeignKey(
        SocialNetwork,
        verbose_name=_("Social Network"),
        on_delete=models.DO_NOTHING,
    )
    social_network_text = models.CharField(
        max_length=125, verbose_name=_("social_network_text"), null=True, blank=True
    )
    phone_number = PhoneNumberField(verbose_name=_("Phone number"))

    def __str__(self):
        return self.name


class Direction(models.Model):
    name = models.CharField(max_length=125, verbose_name=_("Name"))

    def __str__(self):
        return self.name


class QuestionCV(models.Model):
    question = models.CharField(max_length=300, verbose_name=_("question"))

    def __str__(self):
        return self.question


class Answer(models.Model):
    question = models.ForeignKey(
        QuestionCV, verbose_name=_("Question"), on_delete=models.DO_NOTHING
    )
    answer = models.CharField(max_length=300, verbose_name=_("Answer"))

    def __str__(self):
        return self.answer


class CV(models.Model):
    full_name = models.CharField(max_length=125, verbose_name=_("Full Name"))
    email = models.EmailField(verbose_name=_("Email"))
    direction = models.ForeignKey(
        Direction, verbose_name=_("Direction"), on_delete=models.DO_NOTHING
    )
    question = models.ForeignKey(
        QuestionCV, on_delete=models.DO_NOTHING, verbose_name=_("question")
    )
    countries = models.CharField(max_length=225, verbose_name=_("countries"))

    def __str__(self):
        return self.full_name
