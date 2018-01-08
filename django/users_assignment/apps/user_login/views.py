# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from models import *

from django.core import serializers

# Create your views here.
def index(request):
    return render(request, 'user_login/index.html')

def all_json(request):
    users = User_login.objects.all()
    user_json = serializers.serialize('json', users)
    return HttpResponse(user_json, content_type='application/json')

def all_html(request):
    users = User_login.objects.all()
    return render(request, 'user_login/all.html', {'users': users})

def find(request):
    users = User_login.objects.filter(
        first_name__startswith=request.POST['first_name_starts_with']
        )
    print users
    return render(request, 'user_login/all.html', {'users': users})

def create(request):
    User_login.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email_address=request.POST['email_address'],
        age=request.POST['age'],
    )
    users = User_login.objects.order_by('last_name')
    return render(request, 'user_login/all.html', {'users': users})
