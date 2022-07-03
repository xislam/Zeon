from django.db import models
from django.utils.translation import gettext as _


# Create your models here.
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


class UserAnswer(models.Model):
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE)
