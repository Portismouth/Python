# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..users.models import User
from django.db import models

# Create your models here.
class ReviewManager(models.Manager):
    #validates login AND registration
    def book_validator(self, postData):
        errors = []
        # checks if user is registering
        if len(postData['book_title']) < 1:
            errors.append("Please enter a title!")
        if len(postData['book_author']) < 1:
            errors.append("Please please enter an author!")
        if len(postData['book_review']) < 1:
            errors.append("Reviews are important. Please contribute.")
        
        book_exists = Book.objects.filter(title=postData['book_title'])

        if not errors:
            #create or update books
            posted_book_title = postData['book_title']
            if len(book_exists) == 0:
                Book.objects.create(
                    title = postData['book_title'],
                    author = postData['book_author']
                )
            new_book = Book.objects.filter(title=posted_book_title)
            print new_book, "books.models.py line 30"
            reviews = self.create(
                review = postData['book_review'],
                rating = postData['book_rating'],
                book = new_book[0],
                reviewer = User.objects.get(id=postData['user_id'])
            )
            return (True, new_book)
        return (False, errors)

    def recent_and_not(self):
        '''
        returns a tuple with the zeroeth index containing query for 3 most recent reviews, and the first index
        containing the rest
        '''
        return (self.all().order_by('-created_at')[:3], self.all().order_by('-created_at')[3:])

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Review(models.Model):
    review = models.TextField(max_length=1000)
    rating = models.IntegerField()
    book = models.ForeignKey(Book, related_name="reviewed_book")
    reviewer = models.ForeignKey(User, related_name="reviews_left")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ReviewManager()
