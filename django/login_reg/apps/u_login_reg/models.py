# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your models here.

class UserManager(models.Manager):
    def basic_validator(self, postData, action):
        errors = []
        # checks if user is registering
        if action == 'register':
            if len(postData['first_name']) < 1:
                errors.append("Please put in a first name!")
            if len(postData['last_name']) < 1:
                errors.append("Please put in a last name!")
            if len(postData['email']) < 1:
                errors.append("Please enter an email!")
            if not EMAIL_REGEX.match(postData['email']):
                errors.append("Please enter a valid email!")
            if len(postData['password']) < 8:
                errors.append("Please enter a password!")
            if postData['conf_pw'] != postData['password']:
                errors.append("Password must match!!")
        elif action == 'login':
            if len(postData['email']) < 1:
                errors.append("Please enter your email!")
            elif not EMAIL_REGEX.match(postData['email']):
                errors.append("Please enter a valid email!")
            
        email_exists = User.objects.filter(email_address=postData['email'])

        if not errors:
            # checks if user is registering
            if action == 'register': 
                if len(email_exists) != 0:
                    # checks if registering user email already exists
                    errors.append('This user exists!')
                    return (False, errors)
                #otherwise bcrypt password and create user
                hashed_pw = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
                user = User.objects.create(
                    first_name=postData['first_name'],
                    last_name=postData['last_name'],
                    email_address=postData['email'],
                    password=hashed_pw
                )
                return (True, user)
            elif action == 'login':
                #compares user password with posted password
                correct_pw = bcrypt.checkpw(postData['user_password'].encode(), email_exists[0].password.encode())
                #checks if user logging in exists
                if len(email_exists) == 0:
                    #validates whether user actually exists
                    errors.append("This user either doesn't exist or the password is wrong... figure it out.")
                    return (False, errors)
                if correct_pw:
                    user_id = email_exists[0].id
                    return (True, user_id)
                errors.append("This user either doesn't exist or the password is wrong... figure it out.")
                return (False, errors)
        return (False, errors)

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
