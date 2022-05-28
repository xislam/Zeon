from ckeditor.fields import RichTextField
from django.db import models
from django.utils.translation import gettext as _


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
        Country, verbose_name=_("Country"), on_delete=models.CASCADE
    )
    short_description = models.TextField(verbose_name=_("Short description"))
    description = RichTextField(verbose_name=_("Description"))
    remote = models.BooleanField(default=False, verbose_name=_("Remote"))
    office = models.BooleanField(default=False, verbose_name=_("Office"))
    relocation = models.BooleanField(default=False, verbose_name=_("Relocation"))
    date_create = models.DateTimeField(auto_now_add=True, verbose_name=_("Date create"))

    def __str__(self):
        return self.name
