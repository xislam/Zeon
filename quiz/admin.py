from django.contrib import admin
from django.db.models import Case, Count, When, Value, BooleanField, Q

from . import forms
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


@admin.register(models.Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass


class AnswerInline(admin.StackedInline):
    model = models.Answer
    fields = ('question', 'text', 'options', 'point', 'is_checked')
    readonly_fields = ('question', 'text', 'options')

    def get_queryset(self, request):
        qs = super(AnswerInline, self).get_queryset(request)
        qs = qs.filter(is_checked=True)
        return qs

    def has_add_permission(self, request, obj):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(models.Response)
class ResponseAdmin(admin.ModelAdmin):
    readonly_fields = ('is_checked',)
    fields = 'id', 'quiz', 'user', 'total_point', 'created_at', 'is_checked'
    list_display = 'id', 'quiz', 'user', 'total_point', 'is_checked', 'created_at'
    inlines = (AnswerInline,)

    def is_checked(self, obj) -> bool:
        return obj.is_checked

    is_checked.boolean = True

    def get_queryset(self, request):
        qs = super(ResponseAdmin, self).get_queryset(request).annotate(
            unchecked_count=Count(
                'answers__is_checked',
                filter=Q(answers__is_checked=False),
            ),
        ).annotate(
            is_checked=Case(
                When(unchecked_count=0, then=Value(True)),
                default=Value(False),
                output_field=BooleanField(),
            )
        )
        qs = qs.filter(answers__is_checked=True).distinct()
        return qs

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class UncheckedAnswerInline(admin.StackedInline):
    model = models.UncheckedAnswer
    form = forms.UncheckResponseForm
    fields = ('question', 'text', 'options', 'point', 'is_checked')
    readonly_fields = ('question', 'text', 'options')

    def get_queryset(self, request):
        qs = super(UncheckedAnswerInline, self).get_queryset(request)
        qs = qs.filter(is_checked=False)
        return qs

    def has_add_permission(self, request, obj):
        return False

    def has_change_permission(self, request, obj=None):
        return super(UncheckedAnswerInline, self).has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(models.UncheckedResponse)
class UncheckedResponseAdmin(admin.ModelAdmin):
    fields = ('id', 'quiz', 'total_point', 'created_at', 'is_checked')
    list_display = 'id', 'quiz', 'user', 'total_point', 'is_checked', 'created_at'
    readonly_fields = ('id', 'quiz', 'total_point', 'created_at', 'is_checked')
    inlines = (UncheckedAnswerInline,)

    def is_checked(self, obj) -> bool:
        return obj.is_checked

    is_checked.boolean = True

    def get_queryset(self, request):
        qs = super().get_queryset(request).annotate(
            unchecked_count=Count(
                'answers__is_checked',
                filter=Q(answers__is_checked=False),
            ),
        ).annotate(
            is_checked=Case(
                When(unchecked_count=0, then=Value(True)),
                default=Value(False),
                output_field=BooleanField(),
            )
        )
        qs = qs.filter(is_checked=False).distinct()
        return qs

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
