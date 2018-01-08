# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    response = "This will eventually be a list of blogs..."
    return HttpResponse(response)

def new(request):
    response = "This will eventually let you post new blogs..."
    return HttpResponse(response)

def create(request):
    return redirect('/')

def show(request, number):
    response = "This will show blog ", number
    return HttpResponse(response)

def edit(request, number):
    response = "This will edit blog ", number
    return HttpResponse(response)

def destroy(request, number):
    return redirect('/')
