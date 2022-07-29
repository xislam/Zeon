from django.db import models
from django.utils.translation import gettext_lazy as _

from root import settings

from ..choices import Type
from ..choices import Difficulty


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    def __str__(self):
        return self.name


class Topic(models.Model):
    name = models.CharField(max_length=125, verbose_name=_('Name Topic'))

    def __str__(self):
        return self.name


class Quiz(models.Model):
    title = models.CharField(_('title'), max_length=255)
    topics = models.ManyToManyField(
        Topic, related_name='quizzes', verbose_name=_('topics')
    )
    short_description = models.TextField(_('short description'))
    updated_at = models.DateTimeField(_('last updated at'), auto_now=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    class Meta:
        verbose_name = _('quiz')
        verbose_name_plural = _('quiz')
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Question(models.Model):
    quiz = models.ForeignKey('Quiz', models.CASCADE, 'questions')
    type = models.CharField(_('type'), max_length=255, choices=Type.choices)
    title = models.CharField(_('title'), max_length=2000)
    time = models.TimeField(default='00:02:00')
    difficulty = models.IntegerField(
        _('difficulty'), choices=Difficulty.choices, default=Difficulty.MEDIUM
    )
    img = models.ImageField(_('image'), upload_to='q_img', null=True, blank=True)
    updated_at = models.DateTimeField(_('last updated at'), auto_now=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    max_point = models.PositiveSmallIntegerField(_('maximum point'))
    is_active = models.BooleanField(_('is active'), default=False)

    class Meta:
        verbose_name = _('question')
        verbose_name_plural = _('questions')

    def __str__(self):
        return self.title


class Option(models.Model):
    question = models.ForeignKey('Question', models.CASCADE, 'options')
    text = models.CharField(_('text'), max_length=255)
    is_correct = models.BooleanField(_('is correct'), default=False)

    class Meta:
        verbose_name = _('option')
        verbose_name_plural = _('options')

    def __str__(self):
        return self.text


class Response(models.Model):
    quiz = models.ForeignKey('Quiz', models.CASCADE, 'tests')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE, 'tests')
    total_point = models.PositiveSmallIntegerField(_('total point'), default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        pass

    def __str__(self):
        return f'<Response for {self.quiz}> {self.id}'


class Answer(models.Model):
    response = models.ForeignKey('Response', models.CASCADE, 'answers')
    question = models.ForeignKey('Question', models.CASCADE, 'answers')
    text = models.TextField(_('text'), null=True, blank=True)
    options = models.ManyToManyField('Option')
    point = models.PositiveSmallIntegerField(_('point'), default=0)
    is_checked = models.BooleanField(_('is checked'), default=False)

    class Meta:
        unique_together = ('response', 'question')
