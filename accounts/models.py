from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(_("name"), max_length=100)
    email = models.EmailField(_("email address"), unique=True)
    username = models.CharField(_("username"), unique=True, max_length=100)
    otp = models.CharField(_("OTP"), max_length=8, null=True, blank=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["name", "email"]

    objects = CustomUserManager()
