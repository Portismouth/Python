from django import forms
from django.forms import ModelForm, CharField
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from .models import User

# Forms
class RegistrationForm(ModelForm):
    confirm_password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email_address', 'password']
        widgets = {'password': forms.PasswordInput}
