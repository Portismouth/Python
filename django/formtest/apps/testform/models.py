# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django import forms
import bcrypt

# Validators
def validate_name_fields(value):
    if len(value) < 1:
        raise ValidationError(
            _('Please enter a valid name'),
            params={'value': value},
        )

# Create your models here
class User(models.Model):
    first_name = models.CharField(max_length=255, validators=[validate_name_fields])
    last_name = models.CharField(max_length=255)
    email_address = models.EmailField(max_length=255)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
