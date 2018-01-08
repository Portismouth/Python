from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm, CharField
from .models import User

class RegistrationForm(ModelForm):
    confirm_password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']
        widgets = {'password': forms.PasswordInput}

    def clean(self):
        #custom validation for name fields
        if len(self.cleaned_data.get('first_name')) < 1 or len(self.cleaned_data.get('last_name')) < 1:
            print "needs some stuff"
            raise ValidationError(_('Please add something!'), code='required')
        #valdiation for matching password
        if self.cleaned_data.get('confirm_password') != self.cleaned_data.get('password'):
            print "no match"
            raise ValidationError(_('Passwords must match'), code='invalid')
        return self.cleaned_data
