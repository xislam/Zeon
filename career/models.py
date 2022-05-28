from django.db import models
from django.utils.translation import gettext as _


class Category(models.Model):
    name = models.CharField(max_length=125, verbose_name=_("Name"))
    date_create = models.DateTimeField(auto_now_add=True, verbose_name=_("Date create"))

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=125, verbose_name=_("Country"))

    def __str__(self):
        return self.name


class Career(models.Model):
    category = models.ForeignKey(
        Category, verbose_name=_("Category"), on_delete=models.CASCADE
    )
    name = models.CharField(max_length=125, verbose_name=_("Vacancy name"))
    country = models.ForeignKey(
        Country, verbose_name=_("Country"), on_delete=models.CASCADE
    )
    flag = models.ImageField(verbose_name=_("Photo flag"), upload_to="location")
    stack = models.CharField(max_length=125, verbose_name=_("Name steck"))
    date_create = models.DateTimeField(auto_now_add=True, verbose_name=_("Date create"))

    def __str__(self):
        return self.name
