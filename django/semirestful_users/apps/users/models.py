# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your models here.

class UserManager(models.Manager):
    def basic_validator(self, postData, action):
        errors = []
        print type(action)
        if len(postData['first_name']) < 1:
            errors.append("Please put in a first name!")
        elif len(postData['last_name']) < 1:
            errors.append("Please put in a last name!")
        elif len(postData['email_address']) < 1:
            errors.append("Please put in a last name!")
        elif not EMAIL_REGEX.match(postData['email_address']):
            errors.append("Please enter a valid email!")

        email_exists = User.objects.get(email_address=postData['email_address'])
        print email_exists

        if not errors:
            if action == 'create':
                if email_exists:
                    errors.append('This user exists!')
                    return (False, errors)
                user = User.objects.create(
                    first_name=postData['first_name'],
                    last_name=postData['last_name'],
                    email_address=postData['email_address'],
                    )
                return (True, user)
            elif action == 'update':
                user_updating = User.objects.get(id=postData['user_id'])
                user_updating.first_name = postData['first_name']
                user_updating.last_name = postData['last_name']
                user_updating.email_address = postData['email_address']
                user_updating.save()
                return (True, user_updating)
        else:
            return (False, errors)

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
