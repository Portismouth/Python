from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="users"),
    url(r'^new$', views.new, name="new_user"),
    url(r'^create$', views.create_users, name="create_user"),
    url(r'^(?P<user_id>\d+)$', views.show_user, name="show_user"),
    url(r'^(?P<user_id>\d+)/edit$', views.edit, name="edit_user"),
    url(r'^(?P<user_id>\d+)/update$', views.edit_users),
    url(r'^(?P<user_id>\d+)/destroy$', views.destroy),
]
