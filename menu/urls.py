from django.conf.urls import patterns, url

from menu import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='menu'),
)
