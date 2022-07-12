from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import UserCreationForm

from .models import User


class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ("username",)


class UserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = User
        fields = ("email", "username")
