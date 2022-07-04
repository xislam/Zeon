from django.db import models
from django.utils.translation import gettext_lazy as _


class User(models.Model):
    email = models.EmailField()
    otp = models.CharField(max_length=6, null=True, blank=True)
    create_date = models.DateTimeField(
        verbose_name=_("date to check"), auto_now_add=True
    )
    is_verified = models.BooleanField(default=False)
    quiz_title = models.CharField(max_length=225, verbose_name=_("Quiz title"))

    def __str__(self):
        return self.email
