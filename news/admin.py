from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib import admin

from news.models import News


# Register your models here.


class NewsAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = News
        fields = "__all__"


class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm


admin.site.register(News, NewsAdmin)
admin.site.site_header = "ZEON IT HUB"
