# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from .models import User
from django.contrib import messages

# Create your views here.
def index(request):

    if 'name' in request.session:
        return redirect(show_user)
    
    return render(request, "u_login_reg/index.html")

def register(request):
    if 'name' not in request.session:
        print "trying to register"
        valid, response = User.objects.basic_validator(request.POST, 'register')
        print response
        if not valid:
            for error in response:
                messages.error(request, error)
            return redirect('homepage')
        request.session['name'] = request.POST['first_name']
        #how can we get id from newly registered users? 
        request.session['id'] = response.id
        return redirect('show_user')

def login(request):
    if 'name' not in request.session:
        valid, response = User.objects.basic_validator(request.POST, 'login')
        if not valid:
            for error in response:
                messages.error(request, error)
            return redirect('homepage')
        logged_in_user = User.objects.get(id=response)
        request.session['name'] = logged_in_user.first_name
        request.session['id'] = logged_in_user.id
        #be sure to store id so when user creates something we can tie it to a foreign key. Also avoids confusing people with same name
        return redirect('show_user')
    return redirect('homepage')

def logout(request):
    request.session.clear()

    return redirect('homepage')

def show_user(request):
    if 'id' not in request.session:
        messages.error(request, 'Please Login or Register!')
        return redirect('homepage')
    context = {
        'logged_in_user' : request.session['name'],
        'users': User.objects.all()
    }

    return render(request, 'u_login_reg/users.html', context)
