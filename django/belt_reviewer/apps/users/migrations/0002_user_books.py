# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-15 01:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='books',
            field=models.ManyToManyField(related_name='user_books', to='books.Book'),
        ),
    ]
