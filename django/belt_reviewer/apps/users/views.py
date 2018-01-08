# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from .models import User
from ..books.models import Book, Review
from django.contrib import messages

# Create your views here.
def index(request):

    if 'id' in request.session:
        return redirect('users:show_user')

    return render(request, 'users/index.html')

def register(request):
    if 'name' not in request.session:
        print "trying to register"
        valid, response = User.objects.basic_validator(request.POST, 'register')
        print response
        if not valid:
            for error in response:
                messages.error(request, error)
            return redirect('users:homepage')
        request.session['name'] = request.POST['first_name']
        #how can we get id from newly registered users? 
        request.session['id'] = response.id
        return redirect('users:show_user')

def login(request):
    if 'name' not in request.session:
        valid, response = User.objects.basic_validator(request.POST, 'login')
        if not valid:
            for error in response:
                messages.error(request, error)
            return redirect('users:homepage')
        logged_in_user = User.objects.get(id=response)
        request.session['name'] = logged_in_user.first_name
        request.session['id'] = logged_in_user.id
        #be sure to store id so when user creates something we can tie it to a foreign key. Also avoids confusing people with same name
        return redirect('users:show_user')
    return redirect('users:homepage')


def logout(request):
    request.session.clear()

    return redirect('users:homepage')

def show_user(request):
    if 'id' not in request.session:
        messages.error(request, 'Please Login or Register!')
        return redirect('users:homepage')
    user = User.objects.get(id=request.session['id'])
    unique_ids = user.reviews_left.all().values("book").distinct()
    unique_books = []
    for book in unique_ids:
        unique_books.append(Book.objects.get(id=book['book']))
    recent_reviews = Review.objects.recent_and_not
    print recent_reviews
    context = {
        'user': user,
        'user_reviews': unique_books,
        'recent': recent_reviews
    }
    return render(request, 'users/users.html', context)
