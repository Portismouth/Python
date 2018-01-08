# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from .models import User
from django.contrib import messages
# Create your views here.
def index(request):
    context = {
        "users" : User.objects.all(),
    }

    return render(request, "users/index.html", context)

def new(request):
    return render(request, 'users/create.html')


def create_users(request):
    valid, response = User.objects.basic_validator(request.POST, 'create')
    if not valid:
        for error in response:
            messages.error(request, error)
        return redirect('new_user')
    else:
        return redirect("/users")

def show_user(request, user_id):
    context = {
        "user" : User.objects.get(id=user_id)
    }

    return render(request, "users/show.html", context)

def edit(request, user_id):
    context = {
        'user': User.objects.get(id=user_id)
    }

    return render(request, 'users/update.html', context)

def edit_users(request, user_id):
    valid, response = User.objects.basic_validator(request.POST, 'update')
    if not valid:
        for error in response:
            messages.error(request, error)
        return redirect('edit_user', user_id=user_id)
    else:
        return redirect("/users")

def destroy(request, user_id):
    user_deleting = User.objects.get(id=user_id)
    user_deleting.delete()

    return redirect('/users')
