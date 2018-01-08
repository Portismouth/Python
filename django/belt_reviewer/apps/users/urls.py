from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="homepage"),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^profile$', views.show_user, name="show_user"),
    url(r'^logout$', views.logout, name="logout"),
]
