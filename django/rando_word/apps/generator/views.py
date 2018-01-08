# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    
    if 'counter' not in request.session:
        request.session['counter'] = 1

    if 'rando' not in request.session:
        request.session['rando'] = ''

    context = {

    }

    return render(request, 'index.html', context)

def generate(request):

    if request.method == "POST":
        if 'counter' in request.session:
            request.session['counter'] += 1
            request.session['rando'] = get_random_string(length=14)


    return redirect('/')

def reset(request):

    del request.session['counter']
    del request.session['rando']
    return redirect('/')
    
