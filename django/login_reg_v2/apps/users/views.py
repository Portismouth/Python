# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from forms import RegistrationForm
from django.views.generic import View
from .models import User
import bcrypt

# Create your views here.
def index(request):
    context = {
        'form': RegistrationForm()
    }
    return render(request, 'users/index.html', context)

def register(request):
    if request.method == 'POST':
        bound_form = RegistrationForm(request.POST)
        print bound_form.is_valid()
        print bound_form.errors
        return redirect('/')

    return redirect('/')
    
