# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.core import validators
from django.db import models

# Create your models here.
def content_validator(value):
    if len(value) < 1:
        raise ValidationError(
            _('Please enter a valid name'),
            params={'value': value},
        )

class Post(models.Model):
    content = models.TextField(max_length=100, validators=[content_validator])
    created_at = models.DateTimeField(auto_now_add=True)
