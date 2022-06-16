from django.contrib import admin

from partner_site import models


class AnswerInlineModel(admin.TabularInline):
    models
    fields = "__all__"


@admin.register(models.ContactUs)
class QuestionAdmin(admin.ModelAdmin):
    fields = [
        "title",
        "quiz",
    ]
    list_display = ["title", "quiz", "date_updated"]
    inlines = [
        AnswerInlineModel,
    ]
