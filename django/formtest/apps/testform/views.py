# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from forms import RegistrationForm
import bcrypt
# Create your views here.

def index(request):
    bound_form = RegistrationForm(request.POST)
    if request.method == "POST":
        if bound_form.is_valid():
            new_user = bound_form.save(commit=False)
            new_user.password = bcrypt.hashpw(
                bound_form.cleaned_data['password'].encode(), bcrypt.gensalt())
            new_user.save()
            return HttpResponse("Your form is valid")
        else:
            print bound_form.errors.as_data()
            context = {
                'myregistrationform': RegistrationForm(),
                'errors': bound_form.errors
            }
            return render(request, 'testform/index.html', context)
    else:
        context = {
            # Form is the variable name referencing the instance of our RegistrationForm class
            'myregistrationform': RegistrationForm()
        }
        return render(request, 'testform/index.html', context)