# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):

    context = {
    }

    return render(request, 'index.html', context)

def process(request):
    if request.method == "POST":
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['comment'] = request.POST['comment']
    
    return redirect('/result')


def result(request):

    context = {
        'name' : request.session['name']
    }

    return render(request, 'results.html', context)

def reset(request):

    del request.session['name']
    del request.session['location']
    del request.session['comment']

    return redirect('/')
