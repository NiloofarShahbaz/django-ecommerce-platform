from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import RoleChoices
from django.utils.translation import ugettext_lazy as _


class SignUpForm(UserCreationForm):
    # role = forms.ChoiceField(choices=RoleChoices.get_choices(), label=_('نقش'))
    tel = forms.CharField(required=False, label=_('شماره تلفن همراه'))
    address = forms.CharField(required=False, label=_('آدرس'))
    avatar = forms.ImageField(required=False, label=_('تصویر پروفایل'))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'tel', 'address',
                  'avatar']
