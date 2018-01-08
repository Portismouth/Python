# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from .models import Book, Review
from ..users.models import User
from django.contrib import messages

# Create your views here.

def index(request):

    return HttpResponse("Placeholder for recent reviews")

def show_book(request, book_id):
    book = Book.objects.get(id=book_id)
    unique_reviews = book.reviewed_book.all().values('review').distinct()
    print unique_reviews
    context = {
        'book': Book.objects.get(id=book_id),
        'reviews': unique_reviews
    }
    print context, "books.views.py line 21"
    return render(request, 'books/show.html', context)

def new(request):
    context = {
            'logged_in_user_name': request.session['name'],
            'logged_in_user_id': request.session['id'],
        }
    print context, "books.views.py line 31"
    return render(request, 'books/create.html', context)

def create_book(request):
    valid, response = Review.objects.book_validator(request.POST)
    if not valid:
        for error in response:
            messages.error(request, error)
        return redirect('books:new_book')
    book_id = response[0].id
    return redirect('books:show_book', book_id)
