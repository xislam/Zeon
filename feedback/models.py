from django.db import models
from django.utils.translation import gettext as _
from phonenumber_field.modelfields import PhoneNumberField


class Feedback(models.Model):
    name = models.CharField(max_length=125, verbose_name=_("Name"))
    phone_number = PhoneNumberField(verbose_name=_("Phone number"))
    email = models.EmailField(verbose_name=_("Email"))
    status = models.BooleanField(default=False, verbose_name=_("Status"))

    def __str__(self):
        return self.name
