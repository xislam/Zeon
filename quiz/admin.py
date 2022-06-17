from django.contrib import admin

from . import models


@admin.register(models.Category)
class CatAdmin(admin.ModelAdmin):
    list_display = [
        "name",
    ]


@admin.register(models.Quizzes)
class QuizAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
    ]


class AnswerInWritingInlineModel(admin.TabularInline):
    model = models.AnswerInWriting
    fields = ["answer_writing"]


class AnswerInlineModel(admin.TabularInline):
    model = models.Answer
    fields = ["answer_text", "is_right"]


@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ["title", "quiz", "date_updated"]
    inlines = [AnswerInlineModel, AnswerInWritingInlineModel]


@admin.register(models.Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ["answer_text", "is_right", "question"]
