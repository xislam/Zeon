from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import UserCreationForm

from accounts.models import User


class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ("username",)


class UserChangeForm(UserChangeForm):
    class meta:
        model = User
        fields = ("email", "username")
