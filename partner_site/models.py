from django.db import models
from django.utils.translation import gettext as _
from phonenumber_field.modelfields import PhoneNumberField


class Status(models.Model):
    status_name = models.CharField(max_length=125, verbose_name=_("Status name"))

    def __str__(self):
        return self.status_name

    class Meta:
        verbose_name = "Contact Us Partner Status"
        verbose_name_plural = "Contact Us Partner Status"


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
    status = models.ForeignKey(
        Status,
        on_delete=models.DO_NOTHING,
        verbose_name=_("Status"),
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Contact Us Partner"
        verbose_name_plural = "Contact Us Partner"


class SocialNetwork(models.Model):
    name = models.CharField(max_length=125, verbose_name=_("Name"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Social Network Partner"
        verbose_name_plural = "Social Network Partner"


class Direction(models.Model):
    name = models.CharField(max_length=125, verbose_name=_("Name"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Direction Developer"
        verbose_name_plural = "Direction Developer"


class QuestionCV(models.Model):
    question = models.CharField(max_length=300, verbose_name=_("question"))

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "Question CV Developer"
        verbose_name_plural = "Question CV Developer"


class Answer(models.Model):
    answer = models.CharField(max_length=300, verbose_name=_("Answer"))

    def __str__(self):
        return self.answer

    class Meta:
        verbose_name = "Answer Developer"
        verbose_name_plural = "Answer Developer"


class CVStatus(models.Model):
    status_name = models.CharField(max_length=125, verbose_name=_("Status name"))

    def __str__(self):
        return self.status_name

    class Meta:
        verbose_name = "CV Status Developer"
        verbose_name_plural = "CV Status Developer"


class PartnerCV(models.Model):
    full_name = models.CharField(max_length=125, verbose_name=_("Full Name"))
    email = models.EmailField(verbose_name=_("Email"))
    direction = models.CharField(max_length=125, verbose_name=_("Direction"))
    question = models.CharField(max_length=300, verbose_name=_("Question"))
    answer = models.CharField(max_length=300, verbose_name=_("Answer"))
    countries = models.CharField(max_length=225, verbose_name=_("Countries"))
    file_cv = models.FileField(verbose_name=_("File PartnerCV"), upload_to="File_cv_p")
    status = models.ForeignKey(
        Status,
        on_delete=models.DO_NOTHING,
        verbose_name=_("Status"),
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Developer CV"
        verbose_name_plural = "Developer CV"
