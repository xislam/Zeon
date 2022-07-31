from django import forms
from django.utils.translation import gettext_lazy as _

from . import models


class UncheckResponseForm(forms.ModelForm):
    class Meta:
        model = models.UncheckedResponse
        fields = '__all__'

    def save(self, commit=True):
        if isinstance(self.instance, models.UncheckedAnswer):
            if 'is_checked' in self.changed_data:
                self.instance.response.total_point += self.instance.point
                self.instance.response.save()
        super(UncheckResponseForm, self).save(commit)
