from ckeditor.fields import RichTextField
from django.db import models
from django.utils.translation import gettext as _
from phonenumber_field.modelfields import PhoneNumberField


class Direction(models.Model):
    name = models.CharField(max_length=125, verbose_name=_("Name"))
    date_create = models.DateTimeField(auto_now_add=True, verbose_name=_("Date create"))

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=125, verbose_name=_("Country"))
    flag = models.ImageField(verbose_name=_("Photo flag"), upload_to="location")

    def __str__(self):
        return self.name


class Career(models.Model):
    direction = models.ForeignKey(
        Direction, verbose_name=_("Direction"), on_delete=models.CASCADE
    )
    name = models.CharField(max_length=125, verbose_name=_("Vacancy name"))
    country = models.ForeignKey(
        Country,
        verbose_name=_("Country"),
        on_delete=models.CASCADE,
        related_name="country",
    )
    short_description = models.TextField(verbose_name=_("Short description"))
    description = RichTextField(verbose_name=_("Description"))
    remote = models.BooleanField(default=False, verbose_name=_("Remote"))
    office = models.BooleanField(default=False, verbose_name=_("Office"))
    relocation = models.BooleanField(default=False, verbose_name=_("Relocation"))
    date_create = models.DateTimeField(auto_now_add=True, verbose_name=_("Date create"))
    archived = models.BooleanField(verbose_name=_("Archived"), default=False)

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=125, verbose_name=_("Status"))

    def __str__(self):
        return self.name


class CV(models.Model):
    career = models.ForeignKey(
        Career, verbose_name=_("Vacancy"), on_delete=models.DO_NOTHING
    )
    status = models.ForeignKey(
        Status,
        verbose_name=_("Status"),
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING,
    )
    name = models.CharField(max_length=125, verbose_name=_("Name"))
    surname = models.CharField(max_length=125, verbose_name=_("Surname"))
    phone_number = PhoneNumberField(verbose_name=_("Phone number"))
    email = models.EmailField(verbose_name=_("Email"))
    cv_file = models.FileField(verbose_name=_("Summary PartnerCV"), upload_to="CV_file")
    date_create = models.DateTimeField(
        verbose_name=_("Date"), auto_now_add=True, null=True, blank=True
    )

    def __str__(self):
        return self.name
