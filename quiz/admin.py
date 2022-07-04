from django.contrib import admin
from django.contrib.auth.models import User

admin.site.unregister(User)

from . import models


@admin.register(models.Topic)
class TopicAdmin(admin.ModelAdmin):
    fields = ("name",)


@admin.register(models.Category)
class CatAdmin(admin.ModelAdmin):
    list_display = [
        "name",
    ]


class OptionInline(admin.StackedInline):
    model = models.Option
    fields = "text", "is_correct"


@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = (
        "quiz",
        "title",
        "max_point",
        "type",
    )

    inlines = (OptionInline,)


@admin.register(models.Quiz)
class QuizAdmin(admin.ModelAdmin):
    fields = "title", "topics", "short_description"

    list_display = [
        "id",
        "title",
    ]


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    pass
