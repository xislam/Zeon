from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import UserManager
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(_("Name"), max_length=100)
    email = models.EmailField(_("Email"), unique=True)
    username = models.CharField(_("Username"), max_length=100, unique=True)
    password = models.CharField(_("Password"), max_length=255)
    is_staff = models.BooleanField(_("Is staff"), default=False)
    is_superadmin = models.BooleanField(_("Is super admin"), default=False)
    otp = models.CharField(_("OTP"), max_length=6, null=True, blank=True)
    is_active = models.BooleanField(_("Is active"), default=True)
    created_at = models.DateTimeField(_("Create at"), default=timezone.now)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)
    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "username"]

    def __str__(self):
        return self.email
