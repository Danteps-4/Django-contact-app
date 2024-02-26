from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

class UpdateAccountForm(UserChangeForm):
    username = forms.CharField(max_length=250)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")