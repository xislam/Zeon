from ckeditor.fields import RichTextField
from django.db import models
from django.utils.translation import gettext as _


class News(models.Model):
    """Model for News"""

    title = models.CharField(max_length=125, verbose_name=_("Title"))
    short_description = models.TextField(verbose_name=_("Short description"))
    img = models.ImageField(verbose_name=_("Photo for news"), upload_to="news")
    text = RichTextField(verbose_name=_("Text"))
    date_create = models.DateTimeField(verbose_name=_("Create date time"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "News"
