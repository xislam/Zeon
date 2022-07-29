from django.db import models
from django.utils.translation import gettext_lazy as _


class Difficulty(models.IntegerChoices):
    EASY = 1, _('easy')
    MEDIUM = 2, _('medium')
    HARD = 3, _('hard')


class Type(models.TextChoices):
    TEXT = 'text', _('text')
    SELECT = 'select', _('select')
    MULTIPLE = 'multiple', _('multiple choice')
    MULTIPLE_WITH_OWN_ANSWER = 'multiple_own', _('multiple with own answer')
