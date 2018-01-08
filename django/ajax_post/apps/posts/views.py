# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from models import Post
from django.core import serializers
from forms import PostForm
import json

# Create your views here.
def index(request):
    context = {
        'posts': Post.objects.all(),
        'form': PostForm(),
    }
    return render(request, 'posts/index.html', context)


def post(request):
    if request.method == 'POST':
        bound_form = PostForm(request.POST)
    if bound_form.is_valid():
        Post.objects.create(content=request.POST['content'])
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'posts/all.html', context)
