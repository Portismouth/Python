# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

# Create your views here.
def index(request):
    context = {
        "time" : "Today is "+strftime("%A %B %d, %Y")+"and the time is "+strftime("%I:%M %p", gmtime())
    }
    return render(request, 'index.html', context)
