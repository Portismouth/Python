from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.new, name="new_book"),
    url(r'^create$', views.create_book, name="create_book"),
    url(r'^(?P<book_id>\d+)$', views.show_book, name='show_book'),
]
