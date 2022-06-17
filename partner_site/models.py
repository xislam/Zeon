from django.db import models
from django.utils.translation import gettext as _
from phonenumber_field.modelfields import PhoneNumberField


class ContactUs(models.Model):
    name = models.CharField(max_length=125, verbose_name=_("Name"))
    email = models.EmailField(verbose_name=_("Email"))
    social_network = models.CharField(
        max_length=125, verbose_name=_("social_network"), null=True, blank=True
    )
    social_network_text = models.CharField(
        max_length=125, verbose_name=_("social_network_text"), null=True, blank=True
    )
    phone_number = PhoneNumberField(verbose_name=_("Phone number"))

    def __str__(self):
        return self.name


class SocialNetwork(models.Model):
    name = models.CharField(max_length=125, verbose_name=_("Name"))

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
    answer = models.CharField(max_length=300, verbose_name=_("Answer"))

    def __str__(self):
        return self.answer


class PartnerCV(models.Model):
    full_name = models.CharField(max_length=125, verbose_name=_("Full Name"))
    email = models.EmailField(verbose_name=_("Email"))
    direction = models.CharField(max_length=125, verbose_name=_("Direction"))
    question = models.CharField(max_length=300, verbose_name=_("Question"))
    answer = models.CharField(max_length=300, verbose_name=_("Answer"))
    countries = models.CharField(max_length=225, verbose_name=_("Countries"))
    file_cv = models.FileField(verbose_name=_("File PartnerCV"), upload_to="File_cv_p")

    def __str__(self):
        return self.full_name
