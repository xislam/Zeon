import nested_admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UserChangeForm
from .forms import UserCreationForm
from .models import Answer
from .models import Question
from .models import Quiz
from .models import QuizTaker
from .models import User
from .models import UsersAnswer


class AnswerInline(nested_admin.NestedTabularInline):
    model = Answer
    extra = 0


class QuestionInline(nested_admin.NestedTabularInline):
    model = Question
    inlines = [
        AnswerInline,
    ]
    extra = 0


class QuizAdmin(nested_admin.NestedModelAdmin):
    inlines = [
        QuestionInline,
    ]


class UserAnswerInline(admin.TabularInline):
    model = UsersAnswer


class QuizTakerAdmin(admin.ModelAdmin):
    inlines = [UserAnswerInline]


class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ("username", "email", "name", "is_active")
    fieldsets = (
        (None, {"fields": ("name", "username", "email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
    )
    search_fields = ("username",)
    ordering = ("username",)


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(QuizTaker, QuizTakerAdmin)
admin.site.register(UsersAnswer)
admin.site.register(User, UserAdmin)
